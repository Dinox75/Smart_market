#Vai representar uma compra
import json

class Compra:
    def __init__(self, mercado, data, hora):
        self.mercado = mercado
        self.data = data
        self.hora = hora
        self.lista_itens = []
        self.total_compra = 0
        self.total_itens = 0

    def calcular_total_compra(self):
        return sum(item.total_item for item in self.lista_itens)

    def calcular_total_itens(self):
        return sum(item.quantidade for item in self.lista_itens)

    def adicionar_item(self, item):
        self.lista_itens.append(item)
        self.total_compra = self.calcular_total_compra()
        self.total_itens = self.calcular_total_itens()

    def remover_item(self, item):
        if item in self.lista_itens:
            self.lista_itens.remove(item)
            self.total_compra = self.calcular_total_compra()
            self.total_itens = self.calcular_total_itens()
        else:
            print("Item não existe")


    def to_dict(self):
        self.total_compra = self.calcular_total_compra()
        self.total_itens = self.calcular_total_itens()
        
        
        return {
            "mercado": self.mercado,
            "data": self.data,
            "hora": self.hora,
            "total_compra": self.total_compra,
            "total_itens": self.total_itens,
            "itens": [item.to_dict() for item in self.lista_itens]
        
        }

    