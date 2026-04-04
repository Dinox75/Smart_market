#Vai representar uma compra

from .item import Item

class Compra:
    def __init__(self, mercado, data, hora):
        if not mercado or not isinstance(mercado, str):
            raise ValueError("Mercado deve ser uma string não vazia.")
        if not data or not isinstance(data, str):
            raise ValueError("Data deve ser uma string não vazia.")
        if not hora or not isinstance(hora, str):
            raise ValueError("Hora deve ser uma string não vazia.")
        
        self.mercado = mercado
        self.data = data
        self.hora = hora
        self.lista_itens = []

    @property
    def total_compra(self):
        return sum(item.total_item for item in self.lista_itens)

    @property
    def total_itens(self):
        return sum(item.quantidade for item in self.lista_itens)

    def adicionar_item(self, item):
        if not isinstance(item, Item):
            raise TypeError("Item deve ser uma instância da classe Item.")
        self.lista_itens.append(item)

    def remover_item(self, item):
        if item in self.lista_itens:
            self.lista_itens.remove(item)
        else:
            print("Item não existe")

    def to_dict(self):
        return {
            "mercado": self.mercado,
            "data": self.data,
            "hora": self.hora,
            "total_compra": self.total_compra,
            "total_itens": self.total_itens,
            "itens": [item.to_dict() for item in self.lista_itens]
        }

    def __str__(self):
        return f"Compra(mercado='{self.mercado}', data='{self.data}', hora='{self.hora}', total_compra={self.total_compra}, total_itens={self.total_itens})"

    