# 🛒 Smart Market

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
Smart_market/
│
├── main.py
│
├── models/
│ ├── compra.py
│ └── item.py
│
├── utils/
│ └── validacoes.py
│
├── services/
│ ├── historico.py
│ └── comparacoes.py
│
├── data/
│ └── compras.json
│
└── README.md


---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
2. Acesse a pasta
cd Smart_market
3. Execute o projeto
python main.py

💡 Como usar

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

📊 Próximas melhorias
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

✍️ Autor

Vinicius Lima

Projeto desenvolvido com foco em aprendizado prático, evolução profissional e construção de portfólio.