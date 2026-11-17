import json
import math
from datetime import datetime

def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
             
    except FileNotFoundError:
        return []

receitas = carregar_dados("receitas.json")

def registrar_receita():
    descricao = validar_descricao()
    valor = validar_valor()
    data_atual = datetime.now().strftime("%d/%m/%Y")

    receita = {
        "descricao": descricao,
        "valor": valor,
        "data": data_atual
    }

    receitas.append(receita)
    salvar_dados("receitas.json", receitas)
    print("Receita registrada com sucesso!")

def listar_receitas():
    for receita in receitas:
        print(f"Descrição: {receita['descricao']} | Valor: R$ {receita['valor']:.2f}")

def calcular_receitas():
    total = 0

    for receita in receitas:
        total += receita['valor']

    return total

despesas = carregar_dados("despesas.json")

def registrar_despesa():
    descricao = validar_descricao()
    valor = validar_valor()
    categoria = selecionar_categoria()
    data_atual = datetime.now().strftime("%d/%m/%Y")

    despesa = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": data_atual
    }

    despesas.append(despesa)
    salvar_dados("despesas.json", despesas)
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
            if valor <= 0 or not math.isfinite(valor):
                print("Erro! Digite um valor positivo e válido!")
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

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def excluir_dados(dados, nome_arquivo, tipo):
    if not dados:
        print(f"Nenhuma {tipo.lower()} cadastrada.")
        return

    for indice, item in enumerate(dados, start=1):
        print(f"{indice} - {item['descricao']}")

    try:
        opcao = int(input(f"Digite o número da {tipo.lower()} que deseja excluir: "))

        if 1 <= opcao <= len(dados):
            item_selecionado = dados[opcao - 1]

            print("========== MOVIMENTAÇÃO SELECIONADA ==========")
            print(f"Descrição: {item_selecionado['descricao']}")
            print(f"Valor: R$ {item_selecionado['valor']:.2f}")

            if "categoria" in item_selecionado:
                print(f"Categoria: {item_selecionado['categoria']}")

            confirmacao = input(f"Deseja realmente excluir essa {tipo.lower}? (s/n): ").strip().lower()
            if confirmacao == "s":
                dados.pop(opcao - 1)
                salvar_dados(nome_arquivo, dados)
                print(f"{tipo} excluída com sucesso!")
            elif confirmacao == "n":
                print("Exclusão cancelada.")
                return
            else:
                print("Resposta inválida. Exclusão cancelada.")
        else:
            print(f"{tipo} não encontrada.")

    except ValueError:
        print("Erro! Digite um número válido!")

def editar_valor(dados, nome_arquivo, tipo):
    if not dados:
        print(f"Nenhuma {tipo.lower()} cadastrada.")
        return

    for indice, item in enumerate(dados, start=1):
        print(f"{indice} - {item['descricao']} | R$ {item['valor']:.2f}")

    try:
        opcao = int(input(f"Digite o número da {tipo.lower()} que deseja editar: "))

        if 1 <= opcao <= len(dados):
            novo_valor = validar_valor()

            dados[opcao - 1]['valor'] = novo_valor
            salvar_dados(nome_arquivo, dados)
            print(f"{tipo} editada com sucesso!") 

        else:
            print(f"{tipo} não encontrada.")

    except ValueError:
            print("Erro! Digite um número válido!")

def editar_descricao(dados, nome_arquivo, tipo):
    if not dados:
        print(f"Nenhuma {tipo.lower()} cadastrada.")
        return

    for indice, item in enumerate(dados, start=1):
        print(f"{indice} - {item['descricao']}")

    try:
        opcao = int(input(f"Digite o número da {tipo.lower()} que deseja editar: "))

        if 1 <= opcao <= len(dados):

            nova_descricao = validar_descricao()
            dados[opcao - 1]['descricao'] = nova_descricao
            salvar_dados(nome_arquivo, dados)

            print(f"Descrição da {tipo.lower()} editada com sucesso!")

        else:
            print(f"{tipo} não encontrada.")

    except ValueError:
        print("Erro! Digite um número válido!")

def editar_categoria(dados, nome_arquivo):
    if not dados:
        print("Nenhuma despesa cadastrada.")
        return

    for indice, despesa in enumerate(dados, start=1):
        print(f"{indice} - {despesa['descricao']} | Categoria: {despesa['categoria']}")

    try:
        opcao = int(input("Digite o número da despesa que deseja editar: "))

        if 1 <= opcao <= len(dados):
            
            nova_categoria = selecionar_categoria()
            dados[opcao - 1]['categoria'] = nova_categoria
            salvar_dados(nome_arquivo, dados)

            print("Categoria editada com sucesso!")
        else:
            print("Despesa não encontrada.")
    except ValueError:
        print("Erro! Digite um número válido!")

def exibir_menu_edicao():
    print("========== EDITAR DADOS ==========")
    print("1 - Editar receita")
    print("2 - Editar despesa")
    print("3 - Editar descrição da receita")
    print("4 - Editar descrição da despesa")
    print("5 - Editar categoria de despesa")
    print("6 - Voltar ao menu principal")

def menu_edicao():
    while True:
        exibir_menu_edicao()
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            editar_valor(receitas, "receitas.json", "Receita")
        elif opcao == "2":
            editar_valor(despesas, "despesas.json", "Despesa")
        elif opcao == "3":
            editar_descricao(receitas, "receitas.json", "Receita")
        elif opcao == "4":
            editar_descricao(despesas, "despesas.json", "Despesa")
        elif opcao == "5":
            editar_categoria(despesas, "despesas.json")
        elif opcao == "6":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida")

def exibir_menu_exclusao():
    print("========== EXCLUIR DADOS ==========")
    print("1 - Excluir receita")
    print("2 - Excluir despesa")
    print("3 - Voltar ao menu principal")

def menu_exclusao():
    while True:
        exibir_menu_exclusao()
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            excluir_dados(receitas, "receitas.json", "Receita")
        elif opcao == "2":
            excluir_dados(despesas, "despesas.json", "Despesa")
        elif opcao == "3":
            print("Voltando ao menu principal...")
            break
        else: 
            print("Opção inválida")

def exibir_menu():  
    print("========== CONTROLE FINANCEIRO ==========")
    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Consultar saldo")
    print("4 - Listar movimentações")
    print("5 - Relatório por categoria")
    print("6 - Excluir dados")
    print("7 - Editar dados")
    print("8 - Sair")
    

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
        menu_exclusao()
    elif opcao == "7":
        menu_edicao()
    elif opcao == "8":
        print("Saindo...")
        break
    else:
        print("Opção inválida")
