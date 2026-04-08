# ==========================================
# 📦 ARQUIVO: historico.py
# 🎯 RESPONSABILIDADE:
# Gerenciar persistência do histórico de compras em JSON
# Salvar e carregar dados estruturados do sistema
# ==========================================

import json
from pathlib import Path

# ==========================================
# 💾 PERSISTÊNCIA DE DADOS
# ==========================================

# 🔹 Função: obter_caminho_historico
# 📌 Objetivo:
# Determinar caminho absoluto para arquivo de histórico
def obter_caminho_historico():
    return Path(__file__).resolve().parent.parent / "data" / "compras.json"


# 🔹 Função: salvar_compra
# 📌 Objetivo:
# Adicionar nova compra ao histórico JSON existente
def salvar_compra(compra):
    nova_compra = compra.to_dict()
    caminho_arquivo = obter_caminho_historico()
    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)

    if caminho_arquivo.exists():
        with caminho_arquivo.open("r", encoding="utf-8") as arquivo:
            try:
                lista_compras = json.load(arquivo)
            except json.JSONDecodeError:
                lista_compras = []
    else:
        lista_compras = []

    lista_compras.append(nova_compra)

    with caminho_arquivo.open("w", encoding="utf-8") as arquivo:
        json.dump(lista_compras, arquivo, indent=4, ensure_ascii=False)


# 🔹 Função: carregar_compras
# 📌 Objetivo:
# Carregar lista completa de compras do histórico JSON
def carregar_compras():
    caminho_arquivo = obter_caminho_historico()
    if not caminho_arquivo.exists():
        return []

    with caminho_arquivo.open("r", encoding="utf-8") as arquivo:
        try:
            lista_compras = json.load(arquivo)
        except json.JSONDecodeError:
            return []

    return lista_compras
