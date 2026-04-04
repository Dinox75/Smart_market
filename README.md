# 🛒 Smart Market

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Sistema em Python para controle de compras de supermercado, com foco em análise de consumo, variação de preços e organização de histórico.

---

## 🚀 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

- Aprender Python na prática com um projeto real
- Aplicar conceitos de Programação Orientada a Objetos (POO)
- Criar um sistema útil para controle de gastos
- Evoluir para análises inteligentes de consumo
- Construir base para um futuro aplicativo completo

---

## 🧠 Funcionalidades atuais

### 📌 Cadastro de compras
✔️ Registro completo de compras via terminal  
✔️ Adição de múltiplos itens  
✔️ Validação de entradas do usuário  

---

### 📊 Cálculos automáticos
✔️ Total por item  
✔️ Total da compra  
✔️ Quantidade total de itens  

---

### 🏷️ Categorização automática
✔️ Classificação automática de produtos em categorias  
✔️ Armazenamento de categorias em arquivo JSON  
✔️ Suporte a novas categorias dinamicamente  

---

### 💾 Persistência de dados
✔️ Armazenamento em arquivo JSON  
✔️ Histórico acumulado de compras  

---

### 📂 Histórico interativo
✔️ Visualização de todas as compras realizadas  
✔️ Exibição opcional dos itens de cada compra  
✔️ Estrutura organizada para leitura  

---

### 📈 Comparação de compras
✔️ Comparação automática ao registrar nova compra  
✔️ Comparação manual entre as duas últimas compras  

Identifica:

- 📈 Produtos que aumentaram de preço  
- 📉 Produtos que diminuíram  
- ➖ Produtos com preço mantido  
- 🆕 Novos produtos  
- ❌ Produtos removidos  

Além disso:

- Diferença de preço  
- Comparação de quantidade  

---

### 🧭 Menu interativo
✔️ Sistema com navegação por menu  
✔️ Separação clara das funcionalidades  
✔️ Melhor experiência de uso no terminal  

---

## 📂 Estrutura do Projeto
```
Smart_Market/
│
├── main.py
│
├── models/
│ ├── __init__.py
│ ├── compra.py
│ └── item.py
│
├── services/
│ ├── __init__.py
│ ├── historico.py
│ ├── comparacoes.py
│ └── categorizar.py
│
├── utils/
│ ├── __init__.py
│ └── validacoes.py
│
├── interface/
│ ├── __init__.py
│ └── terminal.py
│
├── data/
│ ├── compras.json
│ └── categorias_produtos.json
│
└── README.md
---

## ⚙️ Instalação e Execução

### Pré-requisitos
- Python 3.8 ou superior
- Ambiente virtual (recomendado)

### Passos
1. Clone o repositório
```bash
git clone https://github.com/Dinox75/Smart_market.git
```

2. Acesse a pasta
```bash
cd Smart_Market
```

3. Crie e ative um ambiente virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências
```bash
pip install -r requirements.txt
```

5. Execute o projeto
```bash
python main.py
```

---

## 💡 Como usar

Ao iniciar o sistema, você verá um menu:

1 - Registrar nova compra
2 - Ver histórico
3 - Comparar compras
4 - Sair

📌 Registrar compra

Informe mercado, data e hora
Adicione produtos com quantidade e preço
Veja resumo automático
Comparação com compra anterior (se existir)

📌 Ver histórico

Visualize todas as compras registradas
Opção de ver os itens de cada compra

📌 Comparar compras

Compara automaticamente as duas últimas compras do histórico
Mostra variação de preços e quantidade

---

## 📸 Demonstração

### Menu Principal
```
--- SMART MARKET ---

1 - Registrar nova compra
2 - Ver histórico
3 - Comparar compras
4 - Sair

Escolha uma opção: 1
```

### Exemplo de Registro
```
Digite o mercado: Extra
Data da compra (dd/mm/aaaa): 01/04/2026
Insira a hora da compra: 14:30

Item a adicionar: Banana
Quantos produtos foram comprados?: 2
Informe o preço do produto (unidade): 1.50

Continuar? (s/n): n

--- Resumo da compra ---
Mercado: Extra
Data: 01/04/2026
Hora: 14:30
Total de itens: 2
Total da compra: R$ 3.00
```

---
Comparar qualquer compra do histórico
Análise de consumo por produto
Relatórios mais avançados
Interface gráfica (Web ou Desktop)
Dashboard com gráficos
Leitura de nota fiscal (OCR)
Exportação de relatórios
🧑‍💻 Tecnologias utilizadas
Python 3
JSON (armazenamento de dados)

Programação Orientada a Objetos (POO)

📌 Status do Projeto

🚧 Em desenvolvimento contínuo

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

- Abrir issues para bugs ou sugestões
- Enviar pull requests com melhorias
- Compartilhar ideias para novas funcionalidades

Para contribuir:
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

## ✍️ Autor

Vinicius Lima

Projeto desenvolvido com foco em aprendizado prático, evolução profissional e construção de portfólio.