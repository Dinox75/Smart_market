import json
import os

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
        "Frios e Laticinios": ["leite", "queijo", "iogurte"],
        "Açougue": ["carne", "frango", "peixe"],
        "Mercearia": ["arroz", "feijão"],
        "Massas": ["macarrão", "massa"],
        "Hortifruti": ["alface", "tomate", "banana"],
        "Padaria": ["pão", "bolo", "torta"],
        "Congelados": ["sorvete", "lasanha", "pizza"],
        "Doces e Bolachas": ["chocolate", "biscoito", "doce"],
        "Bebidas": ["refrigerante", "suco", "cerveja"],
        "Temperos e Condimentos": ["sal", "pimenta", "azeite"],
        "Matinais": ["cereal", "granola", "aveia"],
        "Limpeza": ["sabão", "detergente", "desinfetante"],
        "Higiene Pessoal": ["shampoo", "sabonete", "creme dental"],
        "Bebe e Infantil": ["fralda", "papinha", "leite em pó"],
        "Pet": ["ração", "areia"],
        "Descartaveis": ["guardanapo", "prato descartável", "copos descartáveis"],
        "Casa e Cozinha": ["panela", "utensílio", "eletrodoméstico"],
        "Automotivo": ["ferramenta", "acessório automotivo"],
        "Eletronicos": ["lâmpada", "carregador", "fone de ouvido"],
        "Saudaveis e Naturais": ["natural", "integral", "orgânico"]
    }

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


def obter_categoria_produto(nome_produto):
    produto = nome_produto.lower().strip()

    categorias = carregar_categorias()
    
    if produto in categorias:
        return categorias[produto]
    
    categoria = categorizar_produto_com_IA(produto)

    categorias[produto] = categoria
    salvar_categorias(categorias)

    return categoria

def categorizar_produto_com_IA(nome_produto):
    nome_produto = nome_produto.lower().strip()

    # 1. Match simples (categoria no nome)
    for categoria in CATEGORIAS_VALIDAS:
        if categoria.lower() in nome_produto:
            return categoria

    # 2. Palavras-chave
    for categoria, palavras in PALAVRAS_CHAVE.items():
        for palavra in palavras:
            if palavra in nome_produto:
                return categoria

    # 3. (FUTURO) chamada da IA real
    categoria_ia = chamar_ia(nome_produto)

    # 4. Validação
    if categoria_ia in CATEGORIAS_VALIDAS:
        return categoria_ia

    # 5. Fallback
    return "Outros"

def chamar_ia(nome_produto):
    # 🔹 SIMULAÇÃO 
    return "Outros"