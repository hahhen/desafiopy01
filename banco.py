import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[c] Criar conta
[l] Listar contas e usuários
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

def criarUsuário():
    global usuarios
    nome = input("Nome: ")
    data_nasc = datetime.datetime.strptime(input("Data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
    cpf = int(input("CPF: "))
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Sigla estado: ")
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

    
    if not any(usuario['cpf'] == cpf for usuario in usuarios):
        usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nasc": data_nasc,
        "endereco": endereco,
    })
    else:
        print("CPF já cadastrado!")
    
def criarConta():
    global usuarios
    global contas
    cpf = int(input("CPF do titular: "))
    if not any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário não encontrado!")
        return
    index = next((index for (index, d) in enumerate(usuarios) if d["cpf"] == cpf), None)
    contas.append({
        "numero": len(contas) + 1,
        "agencia": "0001",
        "usuario": usuarios[index]
    })

def sacar(*, valor, saldo, limite, extrato, numero_saques):
    if saldo >= valor:
        if valor <= limite:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Limite excedido. O valor máximo para saque é de R$ 500,00.")            
    else:
        print("Saldo insuficiente!")

def depositar(valor, saldo, extrato,/):
    saldo += valor
    extrato += f"Depósito de R$ {valor:.2f}\n"

def mostrarExtrato(saldo,/,*,extrato):
    print(f"Saldo: R$ {saldo:.2f}")
    print("Extrato:")
    print(extrato)

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = abs(float(input("Quanto deseja depositar? ")))
        depositar(valor, saldo, extrato)
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = abs(float(input("Quanto deseja sacar? ")))
            sacar(valor=valor, saldo=saldo, limite=limite, extrato=extrato, numero_saques=numero_saques)
        else:
            print("Limite de saques diários atingido!")
    elif opcao == "e":
        mostrarExtrato(saldo, extrato=extrato)
    elif opcao == "u":
        criarUsuário()
    elif opcao == "c":
        criarConta()
    elif opcao == "l":
        print("Contas:")
        print(contas)
        print("Usuários:")
        print(usuarios)
    elif opcao == "q":
        break
    else:
        print("Opção inválida!")
    