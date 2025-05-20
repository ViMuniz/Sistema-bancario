import textwrap

def menu():
    menu = """\n
    ====== BEM VINDO AO BANCO MOEDA ======
    Seleciona a operação desejada:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair          
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /): #Recebe os argumentos apenas por posição, portanto, tudo antes de "/" deve ser passado por posição
    if valor <= 0:
        print("Operação inválida\n")
        print("=====================================")
        opcao = " "
    else:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("=====================================")
        opcao = " "
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): #Recebe os dados por Keywords (*)
    if numero_saques < limite_saques:
        analise_saque = saldo - valor

        if valor <= 0:
            print("Operação inválida: valor menor ou igual a R$0.00\n")
            print("==================================================")
            opcao = " " 
        
        elif valor > limite:
            print("Operação inválida: valor de saque maior que o limite permitido\n")
            print("==================================================")
            opcao = " "

        elif analise_saque < 0:
            print("Operação inválida: valor de sauqe superior ao valor disponível para saque\n")
            print("==================================================")
            opcao = " "

        elif (0 < valor <= limite) and (analise_saque >= 0):
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R${valor:.2f}\n"
            print("==================================================")
            opcao = " "
    else:
        print(f"Seu limite de {limite_saques} saques diários foi atingido. Faça a operação em outro dia!\n")
        print("==================================================")
        opcao = " "

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n==========EXTRATO===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("\n================================")
    opcao = " "

def criar_usuarios(usuarios):
    cpf = input("Informe seu CPF (apenas números): ") 
    usuario = checagem_usuario_existente(cpf, usuarios) # Usuario será TRUE ou FALSE dependendo da condição da função. E usuarios tem o valor da lista usuario em main()

    if usuario:                                         # Verifica se existe ou não o usuário, caso sim, é pedido novamente a inserção do CPF para análise
        print("Usuário já existente !!!!")
        return  # Sai da função e volta para o menu principal
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (rua, N° - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "edereco": endereco}) # Adiciona no dicionário usuarios[] um novo cadastro sem apagar os já existentes

    print("Usuário cadastrado com sucesso")
    print("==============================")

def checagem_usuario_existente(cpf, usuarios):
    checagem_usuarios = [usuario for usuario in usuarios if usuario["cpf"] == cpf] # Se o campo CPF do usuario que esta sendo percorrido for idêntico, retona o usuário ou a lista fica vázia
    return checagem_usuarios[0] if checagem_usuarios else None # Se a lista "checagem_usuarios" não tem nada = true

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF (apenas números): ") 
    usuario = checagem_usuario_existente(cpf, usuarios) # Usuario será TRUE ou FALSE dependendo da condição da função. E usuarios tem o valor da lista usuario em main()

    if usuario:                                         # Verifica se existe ou não o usuário, caso sim, é pedido novamente a inserção do CPF para análise
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario} # Sai da função e volta para o menu principal
    
    print("Usuário não encontrado! Encerrando criação de novo usuário.")

def listar_contas(contas):
    for conta in contas:
        agencia = conta["agencia"]
        # Acessa o dicionário dentro da lista e pega o valor da chave 'numero_conta'
        numero_conta = conta["numero_conta"][0]['numero_conta'] if conta["numero_conta"] else "N/A"
        nome_titular = conta["usuario"]["nome"]

        print(f"Agência: {agencia}\n C/C: {numero_conta}\nTitular: {nome_titular}\n")
        

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = [] # lista
    contas = []

    while True:
        opcao = menu()

        # DEPÓSITO -------------------------------------------------------------------------------    
        if opcao == "d":
            print("============DEPÓSITO==============")
            valor = float(input("Insira o valor que será depositado em sua conta: R$")) #Insere o valor de depósito
            saldo, extrato = depositar(saldo, valor, extrato) # Retono dos valores saldo e extrato da função depositar por posição

        # SAQUE -------------------------------------------------------------------------------    
        elif opcao == "s":
            print("============SAQUE=============")
            valor = float(input("Insira o valor de saque: R$")) #Insere o valor de saque
            saldo, extrato = sacar( #Envio dos dados para a função "sacar" usando keywords
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        # EXTRATO -------------------------------------------------------------------------------
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato) # Pode chamar a função desse modo também
 
        # NOVA CONTA -------------------------------------------------------------------------------
        elif opcao == "nc":
            numero_conta = len(contas) + 1 # Pega o valor atual da conta (quantos elementos tem ao total) e incrementa 1
            conta = criar_conta(AGENCIA, contas, usuarios) # Envia para a função os valores de cada variável

            if conta:                   # Se a lista não for vázia, então ela é adicinada na lista contas a agencia, conta e usuário
                contas.append(conta)

        # LISTAR CONTAS -------------------------------------------------------------------------------
        elif opcao == "lc":
            listar_contas(contas)

        # NOVO USUÁRIO -------------------------------------------------------------------------------
        elif opcao == "nu":
             criar_usuarios(usuarios) # Envia a lista "usuarios" para a função


        # SAIR -------------------------------------------------------------------------------
        elif opcao == "q":
            break

        else:
            print("Operação escolhida inválida\n")

main()
