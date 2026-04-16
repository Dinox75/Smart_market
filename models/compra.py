# ==========================================
# 📦 ARQUIVO: compra.py
# 🎯 RESPONSABILIDADE:
# Modelo de dados para representar uma compra completa
# Gerencia itens, totais e conversão para dicionário
# ==========================================

from .item import Item


class Compra:
    """
    Representa uma compra com mercado, data, hora e lista de itens.
    """

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
        """
        Soma o total de todos os itens da compra.
        """
        return round(sum(item.total_item for item in self.lista_itens), 2)

    @property
    def total_itens(self):
        """
        Soma a quantidade total de unidades compradas.
        """
        return sum(item.quantidade for item in self.lista_itens)

    def adicionar_item(self, item):
        """
        Adiciona um item à compra.
        """
        if not isinstance(item, Item):
            raise TypeError("Item deve ser uma instância da classe Item.")

        self.lista_itens.append(item)

    def remover_item(self, item):
        """
        Remove um item da compra.
        Retorna True se removeu, False se não encontrou.
        """
        if item in self.lista_itens:
            self.lista_itens.remove(item)
            return True

        return False

    def to_dict(self):
        """
        Converte a compra para dicionário.
        """
        return {
            "mercado": self.mercado,
            "data": self.data,
            "hora": self.hora,
            "total_compra": self.total_compra,
            "total_itens": self.total_itens,
            "itens": [item.to_dict() for item in self.lista_itens]
        }

    def __str__(self):
        return (
            f"Compra(mercado='{self.mercado}', "
            f"data='{self.data}', "
            f"hora='{self.hora}', "
            f"total_compra={self.total_compra}, "
            f"total_itens={self.total_itens})"
        )