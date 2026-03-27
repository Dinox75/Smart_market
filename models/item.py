#Vai representar um item da compra.
import json

class Item:
    def __init__(self, produto, preco_unitario, quantidade):
        self.produto = produto
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.total_item = self.calcular_total_item()

    def calcular_total_item(self):
        return self.preco_unitario * self.quantidade
    
    def to_dict(self):
        pass