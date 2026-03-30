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


def main():
    compra = criar_compra()
    mostrar_resumo(compra)

    historico = carregar_compras()
    if historico:
        ultima_compra = historico[-1]
        resultado = comparar_compras(compra.to_dict(), ultima_compra)
        exibir_relatorio_comparacao(resultado)

    salvar_compra(compra)
    print("Compra salva com sucesso no historico")


if __name__ == "__main__":
    main()