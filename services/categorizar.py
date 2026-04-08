# ==========================================
# 📦 ARQUIVO: categorizar.py
# 🎯 RESPONSABILIDADE:
# Responsável pela categorização inteligente de produtos
# usando cache em JSON, palavras-chave e estrutura para IA
# ==========================================

import json
import os
import unicodedata
import re

# ==========================================
# 📊 CONSTANTES GLOBAIS
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
    "Frios e Laticinios": ["leite", "queijo", "iogurte", "manteiga", "requeijao", "creme", "lacteo"],
    "Açougue": ["carne", "frango", "peixe", "bife", "costela", "linguica", "salsicha"],
    "Mercearia": ["arroz", "feijao", "acucar", "sal", "oleo", "farinha", "trigo", "milho"],
    "Massas": ["macarrao", "massa", "espaguete", "penne", "talharim", "lasanha"],
    "Hortifruti": ["alface", "tomate", "banana", "maca", "laranja", "uva", "batata", "cebola", "alho"],
    "Padaria": ["pao", "bolo", "torta", "bisnaga", "croissant", "pao de forma"],
    "Congelados": ["sorvete", "lasanha", "pizza", "hamburguer", "nugget", "batata frita"],
    "Doces e Bolachas": ["chocolate", "biscoito", "doce", "bolacha", "bala", "caramelo"],
    "Snacks": ["chips", "salgadinho", "pipoca", "amendoim"],
    "Bebidas": ["refrigerante", "suco", "cerveja", "agua", "vinho", "whisky", "vodka", "coca", "cola", "pepsi", "fanta", "guarana", "refri"],
    "Temperos e Condimentos": ["sal", "pimenta", "azeite", "vinagre", "mostarda", "ketchup", "molho"],
    "Matinais": ["cereal", "granola", "aveia", "cafe", "cha", "sucrilhos", "nescau cereal"],
    "Limpeza": ["sabao", "detergente", "desinfetante", "limpa", "esponja", "amaciante"],
    "Higiene Pessoal": ["shampoo", "sabonete", "creme dental", "desodorante", "absorvente"],
    "Bebe e Infantil": ["fralda", "papinha", "leite em po", "chupeta", "mamadeira"],
    "Pet": ["racao", "areia", "brinquedo pet", "coleira"],
    "Descartaveis": ["guardanapo", "prato descartavel", "copos descartaveis", "papel toalha"],
    "Casa e Cozinha": ["panela", "utensilio", "eletrodomestico", "prato", "copo"],
    "Automotivo": ["ferramenta", "acessorio automotivo", "oleo motor"],
    "Eletronicos": ["lampada", "carregador", "fone de ouvido", "bateria"],
    "Saudaveis e Naturais": ["natural", "integral", "organico", "sem gluten", "vegano"]
}


# ==========================================
# 🔧 UTILIDADES
# ==========================================

# 🔹 Função: normalizar_texto
# 📌 Objetivo:
# Padronizar texto removendo acentos, espaços extras e convertendo para minúsculo
# Usado para comparar produtos de forma consistente
def normalizar_texto(texto):
    if not isinstance(texto, str):
        return ""

    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
    texto = texto.lower()
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto


# ==========================================
# 💾 CACHE E PERSISTÊNCIA
# ==========================================

# 🔹 Função: carregar_categorias
# 📌 Objetivo:
# Carregar categorias salvas em JSON para evitar recategorização
# Retorna dicionário vazio se arquivo não existir ou estiver corrompido
def carregar_categorias():
    if not os.path.exists(CAMINHO_CATEGORIAS):
        return {}

    with open(CAMINHO_CATEGORIAS, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


# 🔹 Função: salvar_categorias
# 📌 Objetivo:
# Salvar dicionário de categorias em JSON com formatação legível
# Mantém cache para futuras execuções
def salvar_categorias(categorias):
    with open(CAMINHO_CATEGORIAS, 'w', encoding='utf-8') as f:
        json.dump(categorias, f, ensure_ascii=False, indent=4)


# ==========================================
# 🎯 CORE - CATEGORIZAÇÃO PRINCIPAL
# ==========================================

# 🔹 Função: obter_categoria_produto
# 📌 Objetivo:
# Função principal para categorizar produto, usando cache primeiro
# Se não estiver em cache, categoriza e salva para futuras consultas
def obter_categoria_produto(nome_produto):
    produto_normalizado = normalizar_texto(nome_produto)
    categorias = carregar_categorias()

    if produto_normalizado in categorias:
        return categorias[produto_normalizado]

    categoria = categorizar_produto_com_IA(produto_normalizado)

    categorias[produto_normalizado] = categoria
    salvar_categorias(categorias)

    return categoria


# 🔹 Função: categorizar_produto_com_IA
# 📌 Objetivo:
# Lógica de categorização com fallback: categoria no nome, palavras-chave, IA
# Garante que sempre retorne uma categoria válida
def categorizar_produto_com_IA(nome_produto):
    try:
        # 1. Match com nome da categoria
        for categoria in CATEGORIAS_VALIDAS:
            if normalizar_texto(categoria) in nome_produto:
                return categoria

        # 2. Palavras-chave
        for categoria, palavras in PALAVRAS_CHAVE.items():
            for palavra in palavras:
                if normalizar_texto(palavra) in nome_produto:
                    return categoria

        # 3. IA (desativada)
        categoria_ia = chamar_ia(nome_produto)

        if categoria_ia in CATEGORIAS_VALIDAS:
            return categoria_ia

        return "Outros"

    except Exception as e:
        print(f"Erro na categorização: {e}")
        return "Outros"


# ==========================================
# 🤖 IA (DESATIVADA)
# ==========================================

# 🔹 Função: chamar_ia
# 📌 Objetivo:
# Placeholder para integração futura com IA (ex: OpenAI)
# Atualmente retorna "Outros" e informa que IA está desativada
def chamar_ia(nome_produto):
    print(f"IA desativada. Produto '{nome_produto}' será classificado como 'Outros'.")
    return "Outros"