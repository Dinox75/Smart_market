# ==========================================
# 🔧 NOVA SEÇÃO - CORREÇÃO DE NOMES
# ==========================================

CORRECOES_CONHECIDAS = {
    "coco cola": "coca cola",
    "coca-cola": "coca cola",
    "guarana antartica": "guarana antarctica",
    "guaraná antarctica": "guarana antarctica",
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
    """
    Deixa o nome bonito para exibição.
    """
    palavras = nome.split()

    palavras_formatadas = []
    for p in palavras:
        if p.endswith("lt"):
            palavras_formatadas.append(p.upper())
        else:
            palavras_formatadas.append(p.capitalize())

    return " ".join(palavras_formatadas)


def padronizar_nome_produto(nome):
    """
    Pipeline completo:
    normaliza → corrige → formata
    """
    nome_corrigido = corrigir_nome_produto(nome)
    nome_final = formatar_nome_final(nome_corrigido)
    return nome_final