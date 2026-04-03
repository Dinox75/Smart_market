import json
import os

CAMINHO_CATEGORIAS = 'data/categorias_produtos.json'

def carregar_categorias():
    if not os.path.exists(CAMINHO_CATEGORIAS):
        return {}

    with open(CAMINHO_CATEGORIAS, 'r', encoding='utf-8') as f:
        try:
            categorias = json.load(f)
            return categorias
        except json.JSONDecodeError:
            return {}


def salvar_categorias(categorias):
    with open(CAMINHO_CATEGORIAS, 'w', encoding='utf-8') as f:
        json.dump(categorias, f, ensure_ascii=False, indent=4)
