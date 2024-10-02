import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
LIMITE_TRANSACOES = 10
excedeu_limite = False

while True:
    opcao = input(menu)
    numero_transacoes = 0
    for transacao in extrato:
        if transacao["data"].date() == datetime.datetime.now().date():
            numero_transacoes += 1
        if numero_transacoes >= LIMITE_TRANSACOES:
            excedeu_limite = True
    if opcao == "d":
        if excedeu_limite == False:
            valor = abs(float(input("Quanto deseja depositar? ")))
            saldo += valor
            extrato.append(
                {
                    "info": f"Depósito de R$ {valor:.2f}",
                    "data": datetime.datetime.now(),
                }
            )
        else:
            print("Limite de transações diárias atingido!")
    elif opcao == "s":
        if excedeu_limite == False:
            valor = abs(float(input("Quanto deseja sacar? ")))
            if saldo >= valor:
                if valor <= limite:
                    saldo -= valor
                    extrato.append(
                        {
                            "info": f"Saque de R$ {valor:.2f}",
                            "data": datetime.datetime.now(),
                        }
                    )
                else:
                    print(
                        "Limite excedido. O valor máximo para saque é de R$ 500,00."
                    )
            else:
                print("Saldo insuficiente!")
        else:
            print("Limite de transações diárias atingido!")
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print(f"Saldo: R$ {saldo:.2f}")
        print("Extrato:")
        for item in extrato:
            print(f"{item['data'].strftime('%d/%m/%Y %H:%M:%S')} - {item['info']}")
        print("==========================================")
    elif opcao == "q":
        break
    else:
        print("Opção inválida!")
