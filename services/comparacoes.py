# ==========================================
# 📦 ARQUIVO: comparacoes.py
# 🎯 RESPONSABILIDADE:
# Analisar diferenças entre compras históricas
# Identificar variações de preço, novos/removidos produtos
# ==========================================

# ==========================================
# 📊 ANÁLISE COMPARATIVA
# ==========================================

# 🔹 Função: comparar_compras
# 📌 Objetivo:
# Comparar duas compras e identificar diferenças detalhadas
def comparar_compras(compra_atual, compra_anterior):
    aumentaram = []
    diminuiram = []
    mantiveram = []
    novos_produtos = []
    removidos = []

    produtos_anterior = {item["produto"]: item for item in compra_anterior["itens"]}
    produtos_atual = {item["produto"]: item for item in compra_atual["itens"]}

    for produto, item_atual in produtos_atual.items():
        if produto in produtos_anterior:
            item_anterior = produtos_anterior[produto]
            diferenca_preco = item_atual["preco_unitario"] - item_anterior["preco_unitario"]

            if diferenca_preco > 0:
                aumentaram.append({
                    "produto": produto,
                    "preco_anterior": item_anterior["preco_unitario"],
                    "preco_atual": item_atual["preco_unitario"],
                    "diferenca_preco": diferenca_preco,
                    "quantidade_anterior": item_anterior["quantidade"],
                    "quantidade_atual": item_atual["quantidade"]
                })

            elif diferenca_preco < 0:
                diminuiram.append({
                    "produto": produto,
                    "preco_anterior": item_anterior["preco_unitario"],
                    "preco_atual": item_atual["preco_unitario"],
                    "diferenca_preco": diferenca_preco,
                    "quantidade_anterior": item_anterior["quantidade"],
                    "quantidade_atual": item_atual["quantidade"]
                })

            else:
                mantiveram.append({
                    "produto": produto,
                    "preco_anterior": item_anterior["preco_unitario"],
                    "preco_atual": item_atual["preco_unitario"],
                    "quantidade_anterior": item_anterior["quantidade"],
                    "quantidade_atual": item_atual["quantidade"]
                })

        else:
            novos_produtos.append({
                "produto": produto,
                "preco_atual": item_atual["preco_unitario"],
                "quantidade_atual": item_atual["quantidade"]
            })

    for produto, item_anterior in produtos_anterior.items():
        if produto not in produtos_atual:
            removidos.append({
                "produto": produto,
                "preco_anterior": item_anterior["preco_unitario"],
                "quantidade_anterior": item_anterior["quantidade"]
            })

    return {
        "aumentaram": aumentaram,
        "diminuiram": diminuiram,
        "mantiveram": mantiveram,
        "novos_produtos": novos_produtos,
        "removidos": removidos
    }


# 🔹 Função: exibir_relatorio_comparacao
# 📌 Objetivo:
# Exibir relatório formatado das diferenças encontradas
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