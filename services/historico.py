# ==========================================
# 📦 ARQUIVO: historico.py
# 🎯 RESPONSABILIDADE:
# Gerenciar persistência do histórico de compras em JSON
# Agora com normalização automática de dados
# ==========================================

import json
from pathlib import Path

from utils.validacoes import (
    validar_mercado,
    validar_data,
    validar_hora,
    validar_produto,
    validar_quantidade,
    validar_preco
)
from services.categorizar import obter_categoria_produto


# ==========================================
# 📁 CAMINHO DO ARQUIVO
# ==========================================

def obter_caminho_historico():
    return Path(__file__).resolve().parent.parent / "data" / "compras.json"


# ==========================================
# 🧼 NORMALIZAÇÃO
# ==========================================

def normalizar_item(item_dict):
    """
    Recebe um item em formato dict, valida e devolve limpo.
    """
    produto = validar_produto(item_dict.get("produto"))
    preco_unitario = validar_preco(item_dict.get("preco_unitario"))
    quantidade = validar_quantidade(item_dict.get("quantidade"))

    categoria = item_dict.get("categoria")
    if not categoria or str(categoria).strip() == "":
        categoria = obter_categoria_produto(produto)
    else:
        categoria = str(categoria).strip()

    total_item = round(preco_unitario * quantidade, 2)

    return {
        "produto": produto,
        "preco_unitario": preco_unitario,
        "quantidade": quantidade,
        "categoria": categoria,
        "total_item": total_item
    }


def normalizar_compra(compra_dict):
    """
    Recebe uma compra em formato dict e devolve limpa,
    recalculando totais e corrigindo inconsistências.
    """
    mercado = validar_mercado(compra_dict.get("mercado"))
    data = validar_data(compra_dict.get("data"))   # saída ISO
    hora = validar_hora(compra_dict.get("hora"))

    itens_originais = compra_dict.get("itens", [])
    itens_normalizados = []

    for item in itens_originais:
        try:
            item_limpo = normalizar_item(item)
            itens_normalizados.append(item_limpo)
        except ValueError:
            # ignora item inválido sem quebrar o sistema inteiro
            continue

    total_compra = round(sum(item["total_item"] for item in itens_normalizados), 2)
    total_itens = sum(item["quantidade"] for item in itens_normalizados)

    return {
        "mercado": mercado,
        "data": data,
        "hora": hora,
        "total_compra": total_compra,
        "total_itens": total_itens,
        "itens": itens_normalizados
    }


# ==========================================
# 💾 PERSISTÊNCIA
# ==========================================

def salvar_compra(compra):
    """
    Salva uma nova compra no histórico, normalizando antes.
    """
    caminho_arquivo = obter_caminho_historico()
    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)

    if hasattr(compra, "to_dict"):
        nova_compra = compra.to_dict()
    else:
        nova_compra = compra

    nova_compra = normalizar_compra(nova_compra)

    lista_compras = carregar_compras()
    lista_compras.append(nova_compra)

    with caminho_arquivo.open("w", encoding="utf-8") as arquivo:
        json.dump(lista_compras, arquivo, indent=4, ensure_ascii=False)


def carregar_compras():
    """
    Carrega compras do histórico, normalizando tudo que encontrar.
    """
    caminho_arquivo = obter_caminho_historico()

    if not caminho_arquivo.exists():
        return []

    with caminho_arquivo.open("r", encoding="utf-8") as arquivo:
        try:
            lista_compras = json.load(arquivo)
        except json.JSONDecodeError:
            return []

    if not isinstance(lista_compras, list):
        return []

    compras_normalizadas = []

    for compra in lista_compras:
        try:
            compra_limpa = normalizar_compra(compra)
            compras_normalizadas.append(compra_limpa)
        except ValueError:
            # ignora compras inválidas sem derrubar o sistema
            continue

    return compras_normalizadas