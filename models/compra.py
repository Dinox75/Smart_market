# ==========================================
# 📦 ARQUIVO: compra.py
# 🎯 RESPONSABILIDADE:
# Modelo de dados para representar uma compra completa
# Gerencia itens, totais e conversão para dicionário
# ==========================================

from .item import Item

# ==========================================
# 🏗️ MODELO DE DADOS
# ==========================================

class Compra:
    # 🔹 Classe: Compra
    # 📌 Objetivo:
    # Representar uma compra com mercado, data, hora e lista de itens
    # Fornece propriedades calculadas e métodos de manipulação
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

    # 🔹 Propriedade: total_compra
    # 📌 Objetivo:
    # Calcular valor total da compra somando todos os itens
    @property
    def total_compra(self):
        return sum(item.total_item for item in self.lista_itens)

    # 🔹 Propriedade: total_itens
    # 📌 Objetivo:
    # Calcular quantidade total de itens na compra
    @property
    def total_itens(self):
        return sum(item.quantidade for item in self.lista_itens)

    # 🔹 Método: adicionar_item
    # 📌 Objetivo:
    # Adicionar item à lista de itens da compra
    def adicionar_item(self, item):
        if not isinstance(item, Item):
            raise TypeError("Item deve ser uma instância da classe Item.")
        self.lista_itens.append(item)

    # 🔹 Método: remover_item
    # 📌 Objetivo:
    # Remover item específico da lista de itens
    def remover_item(self, item):
        if item in self.lista_itens:
            self.lista_itens.remove(item)
        else:
            print("Item não existe")

    # 🔹 Método: to_dict
    # 📌 Objetivo:
    # Converter objeto Compra em dicionário para serialização JSON
    def to_dict(self):
        return {
            "mercado": self.mercado,
            "data": self.data,
            "hora": self.hora,
            "total_compra": self.total_compra,
            "total_itens": self.total_itens,
            "itens": [item.to_dict() for item in self.lista_itens]
        }

    # 🔹 Método: __str__
    # 📌 Objetivo:
    # Representação string da compra para debug e logging
    def __str__(self):
        return f"Compra(mercado='{self.mercado}', data='{self.data}', hora='{self.hora}', total_compra={self.total_compra}, total_itens={self.total_itens})"

    