#Validar:
    #nome vazio
    #preço inválido
    #quantidade inválida

def validar_produto():
    while True:
        produto = input("Item a adicionar: ").strip()

        if produto == "":
            print("O nome do produto não pode estar vazio")
            continue

        produto = produto.title()
        return produto


def validar_quantidade():
    while True:
        try:
            quantidade = int(input("Quantos produtos foram comprados?: "))

            if quantidade <= 0:
                print("Favor inserir um valor maior que 0")
                continue

            return quantidade

        except ValueError:
            print("Inserir somente números válidos")


def validar_preco():
    while True:
        try:
            preco_str = input("Informe o preço do produto (unidade): ").strip()
            preco_str = preco_str.replace(",", ".")
            preco_unitario = float(preco_str)

            if preco_unitario <= 0:
                print("Favor inserir um preço maior que 0")
                continue

            return preco_unitario

        except ValueError:
            print("Inserir um preço válido")



