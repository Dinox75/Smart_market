#Compara:
    #preço entre os meses
    #aumento e queda
    #quantidade comprada


def comparar_compras(compra_atual, compra_anterior):
    itens_atual = compra_atual["itens"]
    itens_anterior = compra_anterior["itens"]

    itens_atual_dict = {
        item["produto"]: item
        for item in itens_atual
    }

    itens_anterior_dict = {
        item["produto"]: item
        for item in itens_anterior
    }

    aumentaram = []
    diminuiram = []
    mantiveram = []
    novos_produtos = []
    removidos = []

    for nome_produto in itens_atual_dict:
        if nome_produto in itens_anterior_dict:
            preco_atual = itens_atual_dict[nome_produto]["preco_unitario"]
            preco_anterior = itens_anterior_dict[nome_produto]["preco_unitario"]

            quantidade_atual = itens_atual_dict[nome_produto]["quantidade"]
            quantidade_anterior = itens_anterior_dict[nome_produto]["quantidade"]

            dado_produto = {
                "produto": nome_produto,
                "preco_atual": preco_atual,
                "preco_anterior": preco_anterior,
                "diferenca_preco": preco_atual - preco_anterior,
                "quantidade_atual": quantidade_atual,
                "quantidade_anterior": quantidade_anterior,
                "diferenca_quantidade": quantidade_atual - quantidade_anterior
            }

            if preco_atual > preco_anterior:
                aumentaram.append(dado_produto)
            elif preco_atual < preco_anterior:
                diminuiram.append(dado_produto)
            else:
                mantiveram.append(dado_produto)

        else:
            preco_atual = itens_atual_dict[nome_produto]["preco_unitario"]
            quantidade_atual = itens_atual_dict[nome_produto]["quantidade"]

            dado_produto = {
                "produto": nome_produto,
                "preco_atual": preco_atual,
                "preco_anterior": None,
                "diferenca_preco": None,
                "quantidade_atual": quantidade_atual,
                "quantidade_anterior": None,
                "diferenca_quantidade": None
            }

            novos_produtos.append(dado_produto)

    for nome_produto in itens_anterior_dict:
        if nome_produto not in itens_atual_dict:
            preco_anterior = itens_anterior_dict[nome_produto]["preco_unitario"]
            quantidade_anterior = itens_anterior_dict[nome_produto]["quantidade"]

            dado_produto = {
                "produto": nome_produto,
                "preco_atual": None,
                "preco_anterior": preco_anterior,
                "diferenca_preco": None,
                "quantidade_atual": None,
                "quantidade_anterior": quantidade_anterior,
                "diferenca_quantidade": None
            }

            removidos.append(dado_produto)

    return {
        "aumentaram": aumentaram,
        "diminuiram": diminuiram,
        "mantiveram": mantiveram,
        "novos_produtos": novos_produtos,
        "removidos": removidos
    }

def exibir_relatorio_comparacao(resultado):
    print("\n--- Relatório de Comparação ---")

    if resultado["aumentaram"]:
        print("\nProdutos que aumentaram de preço:")
        for item in resultado["aumentaram"]:
            print(
                f"{item['produto']}: "
                f"R$ {item['preco_anterior']:.2f} -> R$ {item['preco_atual']:.2f} "
                f"(Diferença: R$ {item['diferenca_preco']:+.2f}) | "
                f"Qtd: {item['quantidade_anterior']} -> {item['quantidade_atual']}"
            )

    if resultado["diminuiram"]:
        print("\nProdutos que diminuíram de preço:")
        for item in resultado["diminuiram"]:
            print(
                f"{item['produto']}: "
                f"R$ {item['preco_anterior']:.2f} -> R$ {item['preco_atual']:.2f} "
                f"(Diferença: R$ {item['diferenca_preco']:+.2f}) | "
                f"Qtd: {item['quantidade_anterior']} -> {item['quantidade_atual']}"
            )

    if resultado["mantiveram"]:
        print("\nProdutos que mantiveram o preço:")
        for item in resultado["mantiveram"]:
            print(
                f"{item['produto']}: "
                f"R$ {item['preco_atual']:.2f} | "
                f"Qtd: {item['quantidade_anterior']} -> {item['quantidade_atual']}"
            )

    if resultado["novos_produtos"]:
        print("\nNovos produtos na compra atual:")
        for item in resultado["novos_produtos"]:
            print(
                f"{item['produto']}: "
                f"R$ {item['preco_atual']:.2f} | "
                f"Qtd: {item['quantidade_atual']}"
            )

    if resultado["removidos"]:
        print("\nProdutos removidos da compra anterior:")
        for item in resultado["removidos"]:
            print(
                f"{item['produto']}: "
                f"R$ {item['preco_anterior']:.2f} | "
                f"Qtd: {item['quantidade_anterior']}"
            )

    if (
        not resultado["aumentaram"]
        and not resultado["diminuiram"]
        and not resultado["novos_produtos"]
        and not resultado["removidos"]
    ):
        print("Nenhuma mudança significativa entre as compras.")