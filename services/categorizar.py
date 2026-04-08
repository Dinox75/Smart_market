import json
import os
import unicodedata
import re
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    "Açougue": ["carne", "frango", "peixe", "bife", "costela", "linguiça", "salsicha"],
    "Mercearia": ["arroz", "feijao", "acucar", "açucar", "sal", "oleo", "farinha", "trigo", "milho"],
    "Massas": ["macarrao", "massa", "espaguete", "penne", "talharim", "lasanha"],
    "Hortifruti": ["alface", "tomate", "banana", "maça", "laranja", "uva", "batata", "cebola", "alho"],
    "Padaria": ["pao", "bolo", "torta", "bisnaga", "croissant", "pao de forma"],
    "Congelados": ["sorvete", "lasanha", "pizza", "hamburguer", "nugget", "batata frita"],
    "Doces e Bolachas": ["chocolate", "biscoito", "doce", "bolacha", "bala", "caramelo"],
    "Snacks": ["batata", "chips", "salgadinho", "pipoca", "amendoim"],
    "Bebidas": ["refrigerante", "suco", "cerveja", "agua", "vinho", "whisky", "vodka", "coca", "cola", "pepsi", "fanta", "guarana"],
    "Temperos e Condimentos": ["sal", "pimenta", "azeite", "vinagre", "mostarda", "ketchup", "molho"],
    "Matinais": ["cereal", "granola", "aveia", "cafe", "cha"],
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

def normalizar_texto(texto):
    """
    Normaliza o texto: remove acentos, deixa minúsculo, remove espaços extras.
    """
    if not isinstance(texto, str):
        return ""
    # Remove acentos
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
    # Minúsculo
    texto = texto.lower()
    # Remove espaços extras
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

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
    produto_normalizado = normalizar_texto(nome_produto)

    categorias = carregar_categorias()
    
    if produto_normalizado in categorias:
        return categorias[produto_normalizado]
    
    categoria = categorizar_produto_com_IA(produto_normalizado)

    categorias[produto_normalizado] = categoria
    salvar_categorias(categorias)

    return categoria

def categorizar_produto_com_IA(nome_produto):
    """
    Categoriza o produto seguindo a ordem:
    1. Match com nome da categoria
    2. Match com palavras-chave
    3. Chamada da IA
    4. Validação
    5. Fallback
    """
    try:
        # 1. Match simples (categoria no nome)
        for categoria in CATEGORIAS_VALIDAS:
            if normalizar_texto(categoria) in nome_produto:
                return categoria

        # 2. Palavras-chave
        for categoria, palavras in PALAVRAS_CHAVE.items():
            for palavra in palavras:
                if normalizar_texto(palavra) in nome_produto:
                    return categoria

        # 3. Chamada da IA
        categoria_ia = chamar_ia(nome_produto)

        # 4. Validação
        if categoria_ia in CATEGORIAS_VALIDAS:
            return categoria_ia

        # 5. Fallback
        return "Outros"
    except Exception as e:
        # Garantir que nenhuma exceção quebre o fluxo
        print(f"Erro na categorização: {e}")
        return "Outros"

def chamar_ia(nome_produto):
    try:
        prompt = f"""
Classifique o produto abaixo em apenas UMA categoria da lista.

Categorias válidas:
{", ".join(CATEGORIAS_VALIDAS)}

Produto:
{nome_produto}

Responda apenas com o nome exato de uma categoria da lista.
Se não souber, responda apenas: Outros
"""

        resposta = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        categoria = resposta.output_text.strip()

        if categoria in CATEGORIAS_VALIDAS:
            return categoria

        return "Outros"

    except Exception:
        return "Outros"