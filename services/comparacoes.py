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

    # 🔹 normalizar nomes
    produtos_anterior = {
        normalizar_nome(item.get("produto")): item
        for item in compra_anterior.get("itens", [])
    }

    produtos_atual = {
        normalizar_nome(item.get("produto")): item
        for item in compra_atual.get("itens", [])
    }

    # 🔍 comparar atual com anterior
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

    # 🔍 removidos
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