# ==========================================
# 📦 ARQUIVO: categorizar.py
# ==========================================

import json
import os
import unicodedata
import re

# ==========================================
# 📊 CONSTANTES
# ==========================================

CAMINHO_CATEGORIAS = 'data/categorias_produtos.json'

CATEGORIAS_VALIDAS = [
    "Mercearia",
    "Massas",
    "Açougue",
    "Frios e Laticinios",
    "Padaria",
    "Hortifruti",
    "Congelados",
    "Doces e Bolachas",
    "Snacks",
    "Bebidas",
    "Temperos e Condimentos",
    "Matinais",
    "Limpeza",
    "Higiene Pessoal",
    "Bebe e Infantil",
    "Pet",
    "Descartaveis",
    "Bazar",
    "Automotivo",
    "Casa e Cozinha",
    "Eletronicos",
    "Saudaveis e Naturais",
    "Outros"
]

PALAVRAS_CHAVE = {
    "Frios e Laticinios": ["leite", "queijo", "iogurte", "manteiga", "requeijao", "creme"],
    "Açougue": ["carne", "frango", "peixe", "bife", "costela"],
    "Mercearia": ["arroz", "feijao", "acucar", "sal", "oleo", "farinha"],
    "Massas": ["macarrao", "massa", "espaguete", "penne"],
    "Hortifruti": ["alface", "tomate", "banana", "maca", "laranja", "batata"],
    "Padaria": ["pao", "bolo", "torta"],
    "Congelados": ["sorvete", "pizza", "hamburguer"],
    "Doces e Bolachas": ["chocolate", "biscoito", "bolacha"],
    "Snacks": ["chips", "salgadinho", "pipoca"],
    "Bebidas": ["refrigerante", "suco", "agua", "coca", "cola", "guarana"],
    "Temperos e Condimentos": ["sal", "pimenta", "azeite", "vinagre", "ketchup"],
    "Matinais": ["cereal", "granola", "aveia"],
    "Limpeza": ["sabao", "detergente", "desinfetante"],
    "Higiene Pessoal": ["shampoo", "sabonete", "desodorante"],
    "Bebe e Infantil": ["fralda", "papinha"],
    "Pet": ["racao", "areia"],
    "Descartaveis": ["guardanapo", "copo descartavel"],
    "Casa e Cozinha": ["panela", "prato", "copo"],
    "Automotivo": ["oleo motor"],
    "Eletronicos": ["lampada", "fone"],
    "Saudaveis e Naturais": ["integral", "organico"]
}

# ==========================================
# 🔧 NORMALIZAÇÃO BASE (TEM QUE VIR PRIMEIRO)
# ==========================================

def normalizar_texto(texto):
    if not isinstance(texto, str):
        return ""

    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
    texto = texto.lower()
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

# ==========================================
# 🔧 CORREÇÃO DE NOMES
# ==========================================

CORRECOES_CONHECIDAS = {
    "coco cola": "coca cola",
    "coca-cola": "coca cola",
    "guarana antartica": "guarana antarctica",
    "guarana antarctica": "guarana antarctica",
    "paprica": "paprica",
    "vinagre de maca": "vinagre de maca"
}

def corrigir_nome_produto(nome):
    nome_norm = normalizar_texto(nome)

    for errado, correto in CORRECOES_CONHECIDAS.items():
        if errado in nome_norm:
            nome_norm = nome_norm.replace(errado, correto)

    return nome_norm


def formatar_nome_final(nome):
    palavras = nome.split()

    palavras_formatadas = []
    for p in palavras:
        if p.endswith("lt"):
            palavras_formatadas.append(p.upper())
        else:
            palavras_formatadas.append(p.capitalize())

    return " ".join(palavras_formatadas)


def padronizar_nome_produto(nome):
    nome_corrigido = corrigir_nome_produto(nome)
    nome_final = formatar_nome_final(nome_corrigido)
    return nome_final

# ==========================================
# 💾 CACHE
# ==========================================

def carregar_categorias():
    if not os.path.exists(CAMINHO_CATEGORIAS):
        return {}

    with open(CAMINHO_CATEGORIAS, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def salvar_categorias(categorias):
    with open(CAMINHO_CATEGORIAS, 'w', encoding='utf-8') as f:
        json.dump(categorias, f, ensure_ascii=False, indent=4)

# ==========================================
# 🎯 CATEGORIZAÇÃO
# ==========================================

def obter_categoria_produto(nome_produto):
    nome_padronizado = padronizar_nome_produto(nome_produto)
    produto_normalizado = normalizar_texto(nome_padronizado)

    categorias = carregar_categorias()

    if produto_normalizado in categorias:
        return categorias[produto_normalizado]

    categoria = categorizar_produto(produto_normalizado)

    categorias[produto_normalizado] = categoria
    salvar_categorias(categorias)

    return categoria


def categorizar_produto(nome_produto):
    # 1. nome da categoria
    for categoria in CATEGORIAS_VALIDAS:
        if normalizar_texto(categoria) in nome_produto:
            return categoria

    # 2. palavras-chave
    for categoria, palavras in PALAVRAS_CHAVE.items():
        for palavra in palavras:
            if normalizar_texto(palavra) in nome_produto:
                return categoria

    return "Outros"