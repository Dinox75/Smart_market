#Vai representar um item da compra.

class Item:
    def __init__(self, produto, preco_unitario, quantidade):
        if not produto or not isinstance(produto, str):
            raise ValueError("Produto deve ser uma string não vazia.")
        if preco_unitario <= 0:
            raise ValueError("Preço unitário deve ser maior que zero.")
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")
        
        self.produto = produto
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

    @property
    def total_item(self):
        return self.preco_unitario * self.quantidade
    
    def to_dict(self):
        return {
            "produto": self.produto,
            "preco_unitario": self.preco_unitario,
            "quantidade": self.quantidade,
            "total_item": self.total_item
        }

    def __str__(self):
        return f"Item(produto='{self.produto}', preco_unitario={self.preco_unitario}, quantidade={self.quantidade}, total_item={self.total_item})"