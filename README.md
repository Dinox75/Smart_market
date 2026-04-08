# 🛒 Smart Market

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Sistema em Python para controle de compras de supermercado com histórico em JSON, comparação de compras e categorização inteligente.

---

## 🚀 Sobre o projeto

Smart Market nasceu como um projeto de aprendizado contínuo para construir uma aplicação prática em Python.

O foco principal é:

- registrar compras de supermercado de forma simples;
- manter histórico persistente em JSON;
- comparar compras entre períodos;
- identificar variações de preço e mudanças de portfólio;
- analisar consumo por categoria;
- estruturar o código de forma modular e escalável.

---

## 🧠 O que o projeto faz hoje

### ✅ Funcionalidades atuais

- Registro manual de compras via terminal
- Armazenamento de histórico em `data/compras.json`
- Comparação entre compras históricas
- Identificação de:
  - produtos que aumentaram de preço
  - produtos que diminuíram de preço
  - novos produtos adicionados
  - produtos removidos
- Análise de consumo por categoria
- Categorização automática de produtos com:
  - normalização de texto
  - palavras-chave
  - suporte para integração futura com IA
- Arquitetura modular (`models`, `services`, `utils`, `interface`)

---

## 🧱 Arquitetura do projeto

- `main.py` — ponto de entrada da aplicação e controle de fluxo
- `models/` — classes de domínio (`Compra`, `Item`)
- `services/` — lógica de negócio e persistência
  - `historico.py` — salva e carrega histórico em JSON
  - `comparacoes.py` — compara compras e gera relatórios
  - `categorizar.py` — categorização inteligente de produtos
- `utils/` — funções de validação de entrada do usuário
- `interface/` — ponto inicial para expansão de interface (terminal/web)
- `data/` — arquivos de dados e categorias

---

## ⚙️ Instalação e execução

### Pré-requisitos
- Python 3.8 ou superior
- Ambiente virtual recomendado

### Passos

1. Clone o repositório

```bash
git clone https://github.com/Dinox75/Smart_market.git
```

2. Acesse a pasta do projeto

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

Ao iniciar, o sistema exibe um menu com as seguintes opções:

1. Registrar nova compra
2. Ver histórico
3. Comparar compras
4. Analisar consumo por categoria
5. Sair

### Registrar nova compra
- Informe mercado, data e hora
- Adicione itens com produto, quantidade e preço
- O sistema cria um resumo automático
- A categoria do produto é sugerida com base em regras e palavras-chave

### Ver histórico
- Lista todas as compras registradas
- Permite exibir os itens de cada compra

### Comparar compras
- Compara compras do histórico
- Identifica aumentos, reduções, novos produtos e removidos

### Analisar consumo por categoria
- Exibe as categorias com maior valor acumulado
- Ajuda a entender o padrão de gastos

---

## 🧭 Estrutura de pastas

```text
Smart_Market/
├── main.py
├── README.md
├── requirements.txt
├── data/
│   ├── compras.json
│   └── categorias_produtos.json
├── models/
│   ├── __init__.py
│   ├── compra.py
│   └── item.py
├── services/
│   ├── __init__.py
│   ├── calculos.py
│   ├── categorizar.py
│   ├── comparacoes.py
│   └── historico.py
├── utils/
│   ├── __init__.py
│   └── validacoes.py
└── interface/
    ├── __init__.py
    └── terminal.py
```

---

## 📌 Notas importantes

- A categorização usa um modelo baseado em palavras-chave e normalização de texto.
- O projeto já tem estrutura preparada para receber IA no futuro.
- A interface atual é em terminal, mas a arquitetura foi pensada para facilitar expansão.
- O histórico é persistido em JSON para manter o projeto leve e simples.

---

## 📈 Próximos passos

- integrar IA real para categorização automática
- construir dashboard visual
- implementar leitura de nota fiscal (OCR)
- transformar em app/web interface
- adicionar exportação de relatórios

---

## 🤝 Contribuição

Contribuições são bem-vindas!

- Abra issues para bugs e sugestões
- Envie pull requests com melhorias
- Compartilhe ideias para novas funcionalidades

Fluxo sugerido:

```bash
git checkout -b feature/nova-funcionalidade
# faça suas alterações
git commit -m "feat: descrição da melhoria"
git push origin feature/nova-funcionalidade
```

---

## ✍️ Autor

Vinicius Lima

Projeto desenvolvido como aprendizado contínuo, com foco em evolução técnica e construção de portfólio.

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