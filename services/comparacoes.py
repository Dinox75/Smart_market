#Compara:
    #preço entre os meses
    #aumento e queda
    #quantidade comprada


def comparar_compras(compra_atual, compra_anterior):
    itens_atual = compra_atual["itens"]
    itens_anterior = compra_anterior["itens"]

    itens_atual_dict = {
        item ["produto"]: item
        for item in itens_atual
    }

    itens_anterior_dict = {
        item ["produto"]: item
        for item in itens_anterior
    }
        
    aumentaram = []
    diminuiram = []
    mantiveram = []
    novos_produtos = []

    for nome_produto in itens_atual_dict:
        if nome_produto in itens_anterior_dict:
            preco_atual = itens_atual_dict[nome_produto]["preco_unitario"]
            preco_anterior = itens_anterior_dict[nome_produto]["preco_unitario"]

            if preco_atual > preco_anterior:
                aumentaram.append(nome_produto)
            
            elif preco_atual < preco_anterior:
                diminuiram.append(nome_produto)
        
            else:
                mantiveram.append(nome_produto)
        else:
            novos_produtos.append(nome_produto)
            
    return {
    "aumentaram": aumentaram,
    "diminuiram": diminuiram,
    "mantiveram": mantiveram,
    "novos_produtos": novos_produtos
}