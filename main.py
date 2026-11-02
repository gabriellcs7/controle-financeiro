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
    descricao = validar_descricao()

    valor = validar_valor()

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

    return total

despesas = []

def registrar_despesa():
    descricao = validar_descricao()
    valor = validar_valor()

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

    return total

def consultar_saldo():
    total_receitas = calcular_receitas()
    total_despesas = calcular_despesas()

    saldo = total_receitas - total_despesas

    print(f"Total de receitas: {total_receitas:.2f}")
    print(f"Total de despesas: {total_despesas:.2f}")
    print(f"Saldo disponível: {saldo:.2f}")

def validar_valor():
    while True:
        try:
            valor = float(input("Digite o valor: ").replace(",", "."))
            if valor <= 0:
                print("Erro! O valor deve ser maior que 0.")
            else:
                return valor
        except ValueError:
            print("Erro! Digite um número válido.")

def validar_descricao():
    while True:
        descricao = input("Digite a descrição: ").strip()

        if descricao == "":
            print("Erro! Digite algo na descrição.")
        elif descricao.isdigit():
            print("Erro! A descrição não pode ser apenas um número.")
        else:
            return descricao

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
        print("========== CONSULTAR SALDO ==========")
        consultar_saldo()
    elif opcao == "4":
        print("=========== RECEITAS CADASTRADAS ===========")
        listar_receitas()
        print("--------------------------------------------")
        print(f"Total de receitas: R$ {calcular_receitas():.2f}")
        print("=========== DESPESAS CADASTRADAS ===========")
        listar_despesas()
        print("--------------------------------------------")
        print(f"Total de despesas: R$ {calcular_despesas():.2f}")
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida")