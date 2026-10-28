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

def listar_receitas():
    for receita in receitas:
        print(receita)

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
        print("Registrar receita.")
        
        registrar_receita()

        print("Registrado!")
    elif opcao == "2":
        print("Registrar despesa")
    elif opcao == "3":
        print("Consultar saldo")
    elif opcao == "4":
        print("=========== RECEITAS CADASTRADAS ===========")
        listar_receitas()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida")