# 🛒 Smart Market

Sistema em Python para controle de compras de supermercado, permitindo registrar itens, calcular gastos e armazenar histórico para futuras análises.

---

## 🚀 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

* Aprender desenvolvimento em Python com boas práticas
* Aplicar conceitos de programação orientada a objetos (POO)
* Criar um sistema real de controle de compras
* Construir base para análises futuras (comparação de preços, consumo, etc.)
* Evoluir futuramente para um aplicativo completo

---

## 🧠 Funcionalidades atuais

✔️ Cadastro de compras via terminal
✔️ Adição de múltiplos itens
✔️ Cálculo automático:

* Total por item
* Total da compra
* Quantidade total de itens

✔️ Validação de dados:

* Nome do produto obrigatório
* Quantidade válida (> 0)
* Preço válido (aceita vírgula e ponto)
* Data no formato `dd/mm/aaaa`
* Hora no formato `hh:mm`

✔️ Persistência de dados:

* As compras são salvas em arquivo JSON
* Histórico acumulado de compras

---

## 📂 Estrutura do Projeto

```
Smart_market/
│
├── main.py
│
├── models/
│   ├── compra.py
│   └── item.py
│
├── utils/
│   └── validacoes.py
│
├── services/
│   └── historico.py
│
├── data/
│   └── compras.json
│
└── README.md
```

---

## ⚙️ Como executar

1. Clone o repositório:

```
git clone <URL_DO_REPOSITORIO>
```

2. Acesse a pasta do projeto:

```
cd Smart_market
```

3. Execute o programa:

```
python main.py
```

---

## 💡 Como usar

1. Informe:

   * Nome do mercado
   * Data da compra
   * Hora da compra

2. Adicione itens:

   * Nome do produto
   * Quantidade
   * Preço unitário

3. Continue adicionando itens ou finalize

4. O sistema irá:

   * Mostrar o resumo da compra
   * Salvar automaticamente no histórico

---

## 📊 Próximas melhorias

* Comparação com compras anteriores
* Análise de aumento e queda de preços
* Consumo por produto
* Interface gráfica (GUI ou Web)
* Dashboard com gráficos
* Integração com leitura de nota fiscal (OCR)

---

## 🧑‍💻 Tecnologias utilizadas

* Python 3
* JSON (armazenamento de dados)
* Programação Orientada a Objetos (POO)

---

## 📌 Status do Projeto

🚧 Em desenvolvimento contínuo

---

## ✍️ Autor

Vinicius Lima
Projeto desenvolvido para aprendizado e evolução na área de desenvolvimento de software.

---
