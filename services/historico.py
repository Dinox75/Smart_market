#Salvar e carregar compras do histórico.
import json
import os


def salvar_compra(compra):
    nova_compra = compra.to_dict()
    caminho_arquivo = "data/compras.json"

    #Verfica se o arquivo existe
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            try:
                lista_compras = json.load(arquivo)
            except json.JSONDecodeError:
                lista_compras = []

    else:
        lista_compras = []

    #Adiciona a nova compra
    lista_compras.append(nova_compra)

    #Salva no arquivo
    with open(caminho_arquivo, "w", encoding="utf_8") as arquivo:
        json.dump(lista_compras, arquivo, indent=4, ensure_ascii=False)


