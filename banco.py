menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = abs(float(input("Quanto deseja depositar? ")))
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = abs(float(input("Quanto deseja sacar? ")))
            if saldo >= valor:
                if valor <= limite:
                    saldo -= valor
                    extrato += f"Saque de R$ {valor:.2f}\n"
                    numero_saques += 1
                else:
                    print("Limite excedido. O valor máximo para saque é de R$ 500,00.")
            else:
                print("Saldo insuficiente!")
        else:
            print("Limite de saques diários atingido!")
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print(f"Saldo: R$ {saldo:.2f}")
        print("Extrato:")
        print(extrato)
        print("==========================================")
    elif opcao == "q":
        break
    else:
        print("Opção inválida!")
    