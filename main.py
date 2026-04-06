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
from services.categorizar import obter_categoria_produto


def criar_compra():
    mercado = validar_mercado()
    data_agora = validar_data()
    hora_agora = validar_hora()

    compra = Compra(mercado, data_agora, hora_agora)

    while True:
        produto = validar_produto()
        categoria = obter_categoria_produto(produto)

        quantidade = validar_quantidade()
        preco_unitario = validar_preco()

        item = Item(produto, preco_unitario, quantidade, categoria)
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
    print("3 - Comparar compras")
    print("4 - Analisar consumo por categoria")
    print("5 - Sair")

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
                categoria = item.get("categoria", "Sem categoria")

                print(
                    f"- {item['produto']} ({categoria}) | "
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

    total_anterior = compra1["total_compra"]
    total_atual = compra2["total_compra"]
    diferenca_total = total_atual - total_anterior

    total_itens_anterior = compra1["total_itens"]
    total_itens_atual = compra2["total_itens"]
    diferenca_itens = total_itens_atual - total_itens_anterior

    print("\n--- Comparando as compras escolhidas ---")
    print(f"Compra 1: {compra1['mercado']} - {compra1['data']} às {compra1['hora']}")
    print(f"Compra 2: {compra2['mercado']} - {compra2['data']} às {compra2['hora']}")

    print("\n--- Resumo geral da comparação ---")
    print(f"Total anterior: R$ {total_anterior:.2f}")
    print(f"Total atual: R$ {total_atual:.2f}")
    print(f"Diferença total: R$ {diferenca_total:+.2f}")

    print(f"Total de itens anterior: {total_itens_anterior}")
    print(f"Total de itens atual: {total_itens_atual}")
    print(f"Diferença de itens: {diferenca_itens:+}")

    resultado = comparar_compras(compra2, compra1)
    exibir_relatorio_comparacao(resultado)


def analisar_consumo_por_categoria():
    historico = carregar_compras()

    if not historico:
        print("Nenhuma compra registrada no histórico.")
        return

    consumo_categorias = {}

    for compra in historico:
        for item in compra["itens"]:
            produto = item["produto"]
            quantidade = item["quantidade"]
            valor = item["total_item"]

            if "categoria" in item:
                categoria = item["categoria"]
            else:
                categoria = obter_categoria_produto(produto)

            if categoria not in consumo_categorias:
                consumo_categorias[categoria] = {
                    "quantidade_total": 0,
                    "valor_total": 0.0
                }

            consumo_categorias[categoria]["quantidade_total"] += quantidade
            consumo_categorias[categoria]["valor_total"] += valor

    print("\n--- Consumo por categoria ---")
    for categoria, dados in consumo_categorias.items():
        print(
            f"{categoria}: "
            f"{dados['quantidade_total']} unidades | "
            f"Total gasto: R$ {dados['valor_total']:.2f}"
        )


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
            analisar_consumo_por_categoria()

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()