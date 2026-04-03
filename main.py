# Ponto de entrada do projeto.
# Daqui que tudo começa.

from models.compra import Compra
from models.item import Item
from utils.validacoes import (
    validar_mercado,
    validar_data,
    validar_hora,
    validar_produto,
    validar_quantidade,
    validar_preco
)
from services.historico import carregar_compras, salvar_compra
from services.comparacoes import comparar_compras, exibir_relatorio_comparacao


def criar_compra():
    mercado = validar_mercado()
    data_agora = validar_data()
    hora_agora = validar_hora()

    compra = Compra(mercado, data_agora, hora_agora)

    while True:
        produto = validar_produto()
        quantidade = validar_quantidade()
        preco_unitario = validar_preco()

        item = Item(produto, preco_unitario, quantidade)
        compra.adicionar_item(item)

        continuar = input("Continuar? (s/n): ").lower().strip()

        if continuar == "n":
            break
        elif continuar != "s":
            print("Opção inválida. O programa continuará adicionando itens.")

    return compra


def mostrar_resumo(compra):
    print("\n--- Resumo da compra ---")
    print(f"Mercado: {compra.mercado}")
    print(f"Data: {compra.data}")
    print(f"Hora: {compra.hora}")
    print(f"Total de itens: {compra.total_itens}")
    print(f"Total da compra: R$ {compra.total_compra:.2f}")


def mostrar_menu():
    print("\n--- SMART MARKET ---")
    print("1 - Registrar nova compra")
    print("2 - Ver histórico")
    print("3 - Comparar últimas compras")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ").strip()
    return opcao


def mostrar_historico():
    historico = carregar_compras()

    if not historico:
        print("Nenhuma compra registrada no histórico.")
        return

    print("\n--- Histórico de Compras ---")
    for i, compra in enumerate(historico, start=1):
        print(f"\nCompra {i}")
        print(f"Mercado: {compra['mercado']}")
        print(f"Data: {compra['data']}")
        print(f"Hora: {compra['hora']}")
        print(f"Total de itens: {compra['total_itens']}")
        print(f"Total da compra: R$ {compra['total_compra']:.2f}")

        ver_itens = input("Deseja ver os itens desta compra? (s/n): ").lower().strip()

        if ver_itens == "s":
            print("Itens da compra:")
            for item in compra["itens"]:
                print(
                    f"- {item['produto']} | "
                    f"R$ {item['preco_unitario']:.2f} | "
                    f"Qtd: {item['quantidade']} | "
                    f"Total: R$ {item['total_item']:.2f}"
                )


def comparar_ultimas_compras():
    historico = carregar_compras()

    if len(historico) < 2:
        print("É necessário ter pelo menos duas compras no histórico para comparar.")
        return

    compra_atual = historico[-1]
    compra_anterior = historico[-2]

    print("\n--- Comparando as duas últimas compras ---")
    print(
        f"Compra anterior: {compra_anterior['mercado']} - "
        f"{compra_anterior['data']} às {compra_anterior['hora']}"
    )
    print(
        f"Compra atual: {compra_atual['mercado']} - "
        f"{compra_atual['data']} às {compra_atual['hora']}"
    )

    resultado = comparar_compras(compra_atual, compra_anterior)
    exibir_relatorio_comparacao(resultado)

def comparar_compras_escolhidas():
    historico = carregar_compras()

    if len(historico) < 2:
        print("É necessário ter pelo menos duas compras no histórico para comparar.")
        return

    print("\n--- Compras disponíveis para comparação ---")
    for i, compra in enumerate(historico, start=1):
        print(f"{i} - {compra['mercado']} - {compra['data']} às {compra['hora']}")

    try:
        escolha1 = int(input("Escolha a primeira compra (número): "))
        escolha2 = int(input("Escolha a segunda compra (número): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        return

    if (
        escolha1 < 1 or escolha1 > len(historico)
        or escolha2 < 1 or escolha2 > len(historico)
    ):
        print("Escolha inválida.")
        return

    if escolha1 == escolha2:
        print("Escolha duas compras diferentes para comparar.")
        return

    compra1 = historico[escolha1 - 1]
    compra2 = historico[escolha2 - 1]

    print("\n--- Comparando as compras escolhidas ---")
    print(f"Compra 1: {compra1['mercado']} - {compra1['data']} às {compra1['hora']}")
    print(f"Compra 2: {compra2['mercado']} - {compra2['data']} às {compra2['hora']}")

    resultado = comparar_compras(compra2, compra1)
    exibir_relatorio_comparacao(resultado)

def main():
    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            compra = criar_compra()
            mostrar_resumo(compra)

            historico = carregar_compras()
            compra_atual = compra.to_dict()

            if historico:
                compra_anterior = historico[-1]
                resultado = comparar_compras(compra_atual, compra_anterior)
                exibir_relatorio_comparacao(resultado)

            salvar_compra(compra)
            print("Compra salva com sucesso no histórico.")

        elif opcao == "2":
            mostrar_historico()

        elif opcao == "3":
            comparar_compras_escolhidas()

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()