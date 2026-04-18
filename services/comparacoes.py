# ==========================================
# 📦 ARQUIVO: comparacoes.py
# ==========================================

def normalizar_nome(produto):
    """
    Padroniza o nome do produto para comparação.
    """
    return str(produto).strip().lower()


def comparar_compras(compra_atual, compra_anterior):
    aumentaram = []
    diminuiram = []
    mantiveram = []
    novos_produtos = []
    removidos = []

    produtos_anterior = {
        normalizar_nome(item.get("produto")): item
        for item in compra_anterior.get("itens", [])
    }

    produtos_atual = {
        normalizar_nome(item.get("produto")): item
        for item in compra_atual.get("itens", [])
    }

    for nome_norm, item_atual in produtos_atual.items():
        produto_original = item_atual.get("produto")

        if nome_norm in produtos_anterior:
            item_anterior = produtos_anterior[nome_norm]

            preco_atual = round(item_atual.get("preco_unitario", 0), 2)
            preco_anterior = round(item_anterior.get("preco_unitario", 0), 2)

            diferenca_preco = round(preco_atual - preco_anterior, 2)

            base = {
                "produto": produto_original,
                "preco_anterior": preco_anterior,
                "preco_atual": preco_atual,
                "quantidade_anterior": item_anterior.get("quantidade", 0),
                "quantidade_atual": item_atual.get("quantidade", 0)
            }

            if diferenca_preco > 0:
                base["diferenca_preco"] = diferenca_preco
                aumentaram.append(base)
            elif diferenca_preco < 0:
                base["diferenca_preco"] = diferenca_preco
                diminuiram.append(base)
            else:
                mantiveram.append(base)

        else:
            novos_produtos.append({
                "produto": produto_original,
                "preco_atual": round(item_atual.get("preco_unitario", 0), 2),
                "quantidade_atual": item_atual.get("quantidade", 0)
            })

    for nome_norm, item_anterior in produtos_anterior.items():
        if nome_norm not in produtos_atual:
            removidos.append({
                "produto": item_anterior.get("produto"),
                "preco_anterior": round(item_anterior.get("preco_unitario", 0), 2),
                "quantidade_anterior": item_anterior.get("quantidade", 0)
            })

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