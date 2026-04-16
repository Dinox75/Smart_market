# ==========================================
# 📦 ARQUIVO: validacoes.py
# 🎯 RESPONSABILIDADE:
# Funções utilitárias para validação de dados
# Agora separadas em:
# 1) validações puras (reutilizáveis no terminal, web e saneamento)
# 2) validações interativas (usam input no terminal)
# ==========================================

from datetime import datetime


# ==========================================
# 🧼 FUNÇÕES AUXILIARES
# ==========================================

def limpar_texto(valor):
    """
    Remove espaços extras e garante string.
    """
    if valor is None:
        return ""

    valor = str(valor).strip()
    valor = " ".join(valor.split())
    return valor


# ==========================================
# ✅ VALIDAÇÕES PURAS
# ==========================================

def validar_produto(valor):
    """
    Valida nome do produto.
    Recebe um valor e devolve o produto formatado.
    """
    produto = limpar_texto(valor)

    if produto == "":
        raise ValueError("O nome do produto não pode estar vazio")

    return produto.title()


def validar_quantidade(valor):
    """
    Valida quantidade como inteiro positivo.
    """
    try:
        quantidade = int(valor)
    except (ValueError, TypeError):
        raise ValueError("A quantidade deve ser um número inteiro válido")

    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que 0")

    return quantidade


def validar_preco(valor):
    """
    Valida preço como número positivo.
    Aceita vírgula ou ponto.
    Retorna arredondado em 2 casas.
    """
    if valor is None:
        raise ValueError("O preço não pode estar vazio")

    preco_str = limpar_texto(valor).replace(",", ".")

    try:
        preco_unitario = float(preco_str)
    except (ValueError, TypeError):
        raise ValueError("Insira um preço válido")

    if preco_unitario <= 0:
        raise ValueError("O preço deve ser maior que 0")

    return round(preco_unitario, 2)


def validar_mercado(valor):
    """
    Valida nome do mercado.
    """
    mercado = limpar_texto(valor)

    if mercado == "":
        raise ValueError("O nome do mercado não pode estar vazio")

    return mercado.title()


def validar_data(valor, formato_saida="iso"):
    """
    Valida data nos formatos:
    - dd/mm/aaaa
    - aaaa-mm-dd

    formato_saida:
    - 'iso'   -> YYYY-MM-DD
    - 'br'    -> DD/MM/YYYY
    """
    data = limpar_texto(valor)

    if data == "":
        raise ValueError("A data não pode estar vazia")

    data_obj = None

    formatos_aceitos = ["%d/%m/%Y", "%Y-%m-%d"]

    for formato in formatos_aceitos:
        try:
            data_obj = datetime.strptime(data, formato)
            break
        except ValueError:
            continue

    if data_obj is None:
        raise ValueError("Digite uma data válida nos formatos dd/mm/aaaa ou aaaa-mm-dd")

    if formato_saida == "br":
        return data_obj.strftime("%d/%m/%Y")

    return data_obj.strftime("%Y-%m-%d")


def validar_hora(valor):
    """
    Valida hora no formato HH:MM.
    """
    hora = limpar_texto(valor)

    if hora == "":
        raise ValueError("A hora não pode estar vazia")

    try:
        hora_obj = datetime.strptime(hora, "%H:%M")
    except ValueError:
        raise ValueError("Digite uma hora válida no formato hh:mm")

    return hora_obj.strftime("%H:%M")


# ==========================================
# 💬 VALIDAÇÕES INTERATIVAS (TERMINAL)
# ==========================================

def validar_produto_input():
    while True:
        try:
            return validar_produto(input("Item a adicionar: "))
        except ValueError as erro:
            print(erro)


def validar_quantidade_input():
    while True:
        try:
            return validar_quantidade(input("Quantos produtos foram comprados?: "))
        except ValueError as erro:
            print(erro)


def validar_preco_input():
    while True:
        try:
            return validar_preco(input("Informe o preço do produto (unidade): "))
        except ValueError as erro:
            print(erro)


def validar_mercado_input():
    while True:
        try:
            return validar_mercado(input("Digite o mercado: "))
        except ValueError as erro:
            print(erro)


def validar_data_input(formato_saida="iso"):
    while True:
        try:
            return validar_data(input("Data da compra (dd/mm/aaaa ou aaaa-mm-dd): "), formato_saida=formato_saida)
        except ValueError as erro:
            print(erro)


def validar_hora_input():
    while True:
        try:
            return validar_hora(input("Insira a hora da compra: "))
        except ValueError as erro:
            print(erro)