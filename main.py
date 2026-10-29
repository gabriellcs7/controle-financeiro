receitas = [
    {
        "descricao": "Salário",
        "valor": 1500.000,
    },
    {
        "descricao": "Freelance",
        "valor": 350.00,
    },
    {
        "descricao": "Presente",
        "valor": 100.00
    }
]

def registrar_receita():
    descricao = input("Digite a descrição: ")

    valor = float(input("Digite o valor: ").replace(",", "."))

    receita = {
        "descricao": descricao,
        "valor": valor
    }

    receitas.append(receita)
    print("Receita registrada com sucesso!")

def listar_receitas():
    for receita in receitas:
        print(f"Descrição: {receita['descricao']} | Valor: R$ {receita['valor']:.2f}")

def calcular_receitas():
    total = 0

    for receita in receitas:
        total += receita['valor']

    print(f"Total de receitas: R$ {total:.2f}")

despesas = []

def registrar_despesa():
    descricao = input("Digite a descricao: ")
    valor = float(input("Digite o valor: ").replace(",", "."))

    despesa = {
        "descricao": descricao,
        "valor": valor
    }

    despesas.append(despesa)
    print("Despesa registrada com sucesso!")


def listar_despesas():
    for despesa in despesas:
        print(f"Descrição: {despesa['descricao']} | Valor: R$ {despesa['valor']:.2f}")

def calcular_despesas():
    total = 0

    for despesa in despesas:
        total += despesa['valor']

    print(f"Total de despesas: R$ {total:.2f}")

def exibir_menu():
    print("========== CONTROLE FINANCEIRO ==========")
    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Consultar saldo")
    print("4 - Listar movimentações")
    print("5 - Sair")

while True:
    exibir_menu()
    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        print("========== REGISTRAR RECEITA ==========")
        registrar_receita()
    elif opcao == "2":
        print("========== REGISTRAR DESPESA ==========")
        registrar_despesa()
    elif opcao == "3":
        print("Consultar saldo")
    elif opcao == "4":
        print("=========== RECEITAS CADASTRADAS ===========")
        listar_receitas()
        print("--------------------------------------------")
        calcular_receitas()
        print("=========== DESPESAS CADASTRADAS ===========")
        listar_despesas()
        print("--------------------------------------------")
        calcular_despesas()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida")