# ==========================================
# 📦 ARQUIVO: item.py
# 🎯 RESPONSABILIDADE:
# Modelo de dados para representar um item individual da compra
# Gerencia produto, preço, quantidade, categoria e cálculos
# ==========================================

class Item:
    """
    Representa um item individual de uma compra.
    """

    def __init__(self, produto, preco_unitario, quantidade, categoria):
        if not produto or not isinstance(produto, str):
            raise ValueError("Produto deve ser uma string não vazia.")

        if not isinstance(preco_unitario, (int, float)):
            raise ValueError("Preço unitário deve ser numérico.")

        if not isinstance(quantidade, int):
            raise ValueError("Quantidade deve ser um número inteiro.")

        if preco_unitario <= 0:
            raise ValueError("Preço unitário deve ser maior que zero.")

        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")

        if not categoria or not isinstance(categoria, str):
            raise ValueError("Categoria deve ser uma string não vazia.")

        self.produto = produto
        self.preco_unitario = round(float(preco_unitario), 2)
        self.quantidade = quantidade
        self.categoria = categoria

    @property
    def total_item(self):
        """
        Calcula o valor total do item.
        """
        return round(self.preco_unitario * self.quantidade, 2)

    def to_dict(self):
        """
        Converte o item para dicionário.
        """
        return {
            "produto": self.produto,
            "preco_unitario": self.preco_unitario,
            "quantidade": self.quantidade,
            "categoria": self.categoria,
            "total_item": self.total_item
        }

    def __str__(self):
        return (
            f"Item(produto='{self.produto}', "
            f"preco_unitario={self.preco_unitario}, "
            f"quantidade={self.quantidade}, "
            f"categoria='{self.categoria}', "
            f"total_item={self.total_item})"
        )