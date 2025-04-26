# Variáveis
saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(""" ====== BEM VINDO AO BANCO MOEDA ======
                  Seleciona a operação desejada:
                  [d] Depositar
                  [s] Sacar
                  [e] Extrato
                  [q] Sair
                  """)
    
    # DEPÓSITO -------------------------------------------------------------------------------    
    if opcao == "d":
        print("============DEPÓSITO==============")
        deposito = float(input("Insira o valor que será depositado em sua conta: R$"))

        if deposito <= 0:
            print("Operação inválida\n")
            opcao = " "
        else:
            saldo += deposito
            print(f"Operação concluída com exito. Seu novo saldo é de R${saldo:.2f}\n")
            extrato += f"Depósito: R${deposito:.2f}\n"
            opcao = " "

    # SAQUE -------------------------------------------------------------------------------    
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            print("============SAQUE=============")
            saque = float(input("Insira o valor de saque: R$"))
            analise_saque = saldo - saque

            if saque <= 0:
                print("Operação inválida: valor menor ou igual a R$0.00\n")
                opcao = " " 
            
            elif saque > limite_saque:
                print("Operação inválida: valor de saque maior que o limite permitido\n")
                opcao = " "

            elif analise_saque < 0:
                print("Operação inválida: valor de sauqe superior ao valor disponível para saque\n")
                opcao = " "

            elif (0 < saque <= limite_saque) and (analise_saque >= 0):
                saldo -= saque
                numero_saques += 1
                print(f"Operação concluída com sucesso. Seu novo saldo é de {saldo:.2f}\n")
                extrato += f"Saque: R${saque:.2f}\n"
                opcao = " "
        else:
            print(f"Seu limite de {numero_saques} saques diários foi atingido. Faça a operação em outro dia!\n")
            opcao = " "
    
    # EXTRATO -------------------------------------------------------------------------------
    elif opcao == "e":
        print("\n==========EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("==================================\n")
        opcao = " "

    # SAIR -------------------------------------------------------------------------------
    elif opcao == "q":
        break

    else:
        print("Operação escolhida inválida\n")
