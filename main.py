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
    elif opcao == "2":
        print("Registrar despesa")
    elif opcao == "3":
        print("Consultar saldo")
    elif opcao == "4":
        print("Listar movimentações")
    elif opcao == "5":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida")