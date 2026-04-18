from models.compra import Compra
from models.item import Item
from utils.validacoes import (
    validar_mercado_input,
    validar_data_input,
    validar_hora_input,
    validar_produto_input,
    validar_quantidade_input,
    validar_preco_input
)
from services.historico import carregar_compras, salvar_compra
from services.comparacoes import comparar_compras, exibir_relatorio_comparacao
from services.categorizar import obter_categoria_produto, padronizar_nome_produto


def criar_compra():
    mercado = validar_mercado_input()
    data_agora = validar_data_input()  # agora já salva em ISO
    hora_agora = validar_hora_input()

    compra = Compra(mercado, data_agora, hora_agora)

    while True:
        produto = validar_produto_input()
        produto = padronizar_nome_produto(produto)
        categoria = obter_categoria_produto(produto)

        quantidade = validar_quantidade_input()
        preco_unitario = validar_preco_input()

        item = Item(produto, preco_unitario, quantidade, categoria)
        compra.adicionar_item(item)

        continuar = input("Continuar? (s/n): ").strip().lower()

        if continuar == "n":
            break
        elif continuar != "s":
            print("Opção inválida. Continuando...")

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

    return input("Escolha uma opção: ").strip()


def mostrar_historico():
    historico = carregar_compras()

    if not historico:
        print("Nenhuma compra registrada.")
        return

    print("\n--- Histórico de Compras ---")

    for i, compra in enumerate(historico, start=1):
        print(f"\nCompra {i}")
        print(f"Mercado: {compra['mercado']}")
        print(f"Data: {compra['data']}")
        print(f"Hora: {compra['hora']}")
        print(f"Total de itens: {compra['total_itens']}")
        print(f"Total: R$ {compra['total_compra']:.2f}")

        ver_itens = input("Ver itens? (s/n): ").strip().lower()

        if ver_itens == "s":
            for item in compra["itens"]:
                categoria = item.get("categoria", "Sem categoria")

                print(
                    f"- {item['produto']} ({categoria}) | "
                    f"R$ {item['preco_unitario']:.2f} | "
                    f"Qtd: {item['quantidade']} | "
                    f"Total: R$ {item['total_item']:.2f}"
                )


def comparar_compras_escolhidas():
    historico = carregar_compras()

    if len(historico) < 2:
        print("Necessário pelo menos 2 compras.")
        return

    print("\n--- Compras disponíveis ---")

    for i, compra in enumerate(historico, start=1):
        print(f"{i} - {compra['mercado']} - {compra['data']} às {compra['hora']}")

    try:
        c1 = int(input("Primeira compra: "))
        c2 = int(input("Segunda compra: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if c1 < 1 or c2 < 1 or c1 > len(historico) or c2 > len(historico):
        print("Escolha inválida.")
        return

    compra1 = historico[c1 - 1]
    compra2 = historico[c2 - 1]

    resultado = comparar_compras(compra2, compra1)
    exibir_relatorio_comparacao(resultado)


def analisar_consumo_por_categoria():
    historico = carregar_compras()

    if not historico:
        print("Nenhum dado.")
        return

    consumo = {}

    for compra in historico:
        for item in compra["itens"]:
            categoria = item.get("categoria") or obter_categoria_produto(item["produto"])

            if categoria not in consumo:
                consumo[categoria] = 0

            consumo[categoria] += item["total_item"]

    print("\n--- Top 3 categorias ---")

    top = sorted(consumo.items(), key=lambda x: x[1], reverse=True)[:3]

    for i, (cat, valor) in enumerate(top, start=1):
        print(f"{i}º {cat} - R$ {valor:.2f}")


def main():
    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            compra = criar_compra()
            mostrar_resumo(compra)

            historico = carregar_compras()
            atual = compra.to_dict()

            if historico:
                anterior = historico[-1]
                resultado = comparar_compras(atual, anterior)
                exibir_relatorio_comparacao(resultado)

            salvar_compra(compra)
            print("Compra salva.")

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