menu = """
[1] depositar
[2] sacar
[3] extrato
[0] sair 
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3


while True:

    opcao = (input(menu))

    if opcao == "1":
        valor  = float(input("Informe o valor de depósito: "))
        if valor > 0:
            valor += saldo
            extrato += f'Deposito: R$ {valor:.2f}.\n'
        else:
            print("Operação Falhou! O valor informado é inválido.")
               


    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE
        if excedeu_saldo:
            print("A operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("A  operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("A operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}.\n'
            numero_saques += 1
        else:
            print("A operação falhou! O valor informado é inválido.")    


    elif opcao == "3":
        print("\n********EXTRATO********")
        print("Não houve movimentações." if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}.')
        print("***********************")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, favor selecionar novamente a operação desejada.")


