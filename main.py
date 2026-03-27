#Ponto de entrada do projeto.
#Daqui que tudo começa.
from models.compra import Compra
from models.item import Item

mercado = input("Digite o mercado: ")
data_agora = input("Data da compra: ")
hora_agora = input("Hora da compra: ")

compra = Compra(mercado, data_agora, hora_agora)

while True:
    produto = input("Item a adicionar: ")
    quantidade = int(input("Quantos produtos foram comprados?: "))
    
    preco_str = input("Informe o preço do produto(unidade): ")
    preco_str = preco_str.replace(",", ".")
    preco_unitario = float(preco_str)

    item = Item(produto, preco_unitario, quantidade)
    compra.adicionar_item(item)

    continuar = input("Continuar?(s/n): ").lower()


    if continuar == "s":
        continue
    if continuar == "n":
        break

print(f"Total de itens: {compra.total_itens}")
print(f"Total da compra: R$ {compra.total_compra:.2f}")
