import json

def carregar_despesas():
    try:
        with open("despesas.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados

    except FileNotFoundError:
        return []

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

despesas = carregar_despesas()

def registrar_despesa():
    descricao = validar_descricao()
    valor = validar_valor()
    categoria = selecionar_categoria()

    despesa = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria
    }

    despesas.append(despesa)
    salvar_despesas()
    print("Despesa registrada com sucesso!")


def listar_despesas():
    for despesa in despesas:
        print(f"Descrição: {despesa['descricao']} | Valor: R$ {despesa['valor']:.2f} | Categoria: {despesa['categoria']}")

def calcular_despesas():
    total = 0

    for despesa in despesas:
        total += despesa['valor']

    return total

def consultar_saldo():
    total_receitas = calcular_receitas()
    total_despesas = calcular_despesas()

    saldo = total_receitas - total_despesas

    print(f"Total de receitas: R$ {total_receitas:.2f}")
    print(f"Total de despesas: R$ {total_despesas:.2f}")
    print(f"Saldo disponível: R$ {saldo:.2f}")

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

def selecionar_categoria():
    print("========== CATEGORIAS ==========")
    print("1 - Alimentação")
    print("2 - Transporte")
    print("3 - Moradia")
    print("4 - Lazer")
    print("5 - Saúde")
    print("6 - Educação")
    print("7 - Tecnologia")
    print("8 - Outros")

    while True:
        opcao = input("Selecione uma opção: ") 
    
        if opcao == "1":
            return "Alimentação"
        elif opcao == "2":
            return "Transporte"
        elif opcao == "3":
            return "Moradia"
        elif opcao == "4":
            return "Lazer"
        elif opcao == "5":
            return "Saúde"
        elif opcao == "6":
            return "Educação"
        elif opcao == "7":
            return "Tecnologia"
        elif opcao == "8":
            return "Outros"
        else:
            print("Opção inválida")

def relatorio_categorias():
    totais = {}

    if not despesas:
        print("Nenhuma despesa cadastrada")
        return

    for despesa in despesas:
        categoria = despesa["categoria"]
        valor = despesa["valor"]

        if categoria in totais:
            totais[categoria] += valor
        else:
            totais[categoria] = valor

    print("========== RELATÓRIO POR CATEGORIA ==========")

    for categoria, valor in totais.items():

        print(f"{categoria}: R${valor:.2f}")

def salvar_despesas():
    with open("despesas.json", "w", encoding="utf-8") as arquivo:
        json.dump(despesas, arquivo, indent=4, ensure_ascii=False)
        
    print("Despesas salvas com sucesso!")

def exibir_menu():
    print("========== CONTROLE FINANCEIRO ==========")
    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Consultar saldo")
    print("4 - Listar movimentações")
    print("5 - Relatório por categoria")
    print("6 - Sair")

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
        relatorio_categorias()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida")