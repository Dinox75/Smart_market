# 🛒 Smart Market - Controle Inteligente de Compras

Uma aplicação web moderna para gerenciar, analisar e comparar suas compras de supermercado com sincronização em tempo real.

## ✨ Características Principais

### 📊 Dashboard Interativo
- Visualize em tempo real suas métricas de gasto
- Gráficos dinâmicos para análise visual
- Atualização automática a cada 5 segundos

### 💾 Registro de Compras
- Adicione compras com itens, preços e quantidades
- Detecção automática de categorias
- Validação de dados em tempo real

### 📈 Análise e Comparação
- Compare duas compras para entender variações
- Análise completa por categorias
- Histórico detalhado de todas as compras

### 🔄 Sincronização em Tempo Real
- Dados atualizam automaticamente no dashboard
- Sem necessidade de atualizar a página
- Indicador visual de status em tempo real

## 🚀 Como Iniciar

### Pré-requisitos
- Python 3.7+
- pip (gerenciador de pacotes)

### Instalação

1. **Ativar ambiente virtual**
```bash
.\venv\Scripts\Activate.ps1
```

2. **Instalar dependências**
```bash
pip install -r requirements.txt
```

3. **Iniciar o servidor**
```bash
python app.py
```

4. **Abrir no navegador**
```
http://localhost:5000
```

## 📱 Seções da Aplicação

### 🎯 Dashboard
- **Total de Compras**: Número de compras registradas
- **Gasto Total**: Valor acumulado de todas as compras
- **Média por Compra**: Ticket médio
- **Categoria Destaque**: Categoria com maior gasto
- **Gráficos**: Visualizações interativas dos dados

### ➕ Registrar Compra
1. Preencha o **mercado** (ex: Carrefour, Pão de Açúcar)
2. Selecione a **data** e **hora**
3. Adicione **itens** com:
   - Nome do produto
   - Categoria (detectada automaticamente)
   - Preço unitário
   - Quantidade
4. Clique em **"Salvar Compra"**

### 📜 Histórico
- Visualize todas as compras registradas
- Clique em uma compra para ver detalhes
- Mostra mercado, data, hora e valor total

### ⚖️ Comparar Compras
1. Selecione duas compras
2. Clique em **"Comparar"**
3. Veja a análise:
   - Valores de cada compra
   - Diferença absoluta
   - Variação percentual

### 📊 Análise de Consumo
- Top 10 categorias por gasto
- Percentual de cada categoria
- Valor médio por compra
- Barras de progresso visuais

### ℹ️ Sobre o Projeto
- Informações completas sobre a aplicação
- Fluxo de funcionamento
- Tecnologias utilizadas
- Instruções de uso

## 🎨 Design

A aplicação utiliza um design moderno com:
- **Paleta de cores**: Verde primário, azul secundário, laranja destaque
- **Responsividade**: Funciona em desktop, tablet e mobile
- **Animações**: Transições suaves e feedback visual
- **Acessibilidade**: Contraste adequado e ícones intuitivos

## 🔧 Estrutura do Projeto

```
Smart_Market/
├── app.py                    # Servidor Flask
├── index.html               # Interface web (refatorado)
├── requirements.txt         # Dependências Python
├── models/
│   ├── compra.py           # Modelo de Compra
│   └── item.py             # Modelo de Item
├── services/
│   ├── calculos.py         # Cálculos de compras
│   ├── categorizar.py      # Categorização automática
│   ├── comparacoes.py      # Comparação entre compras
│   └── historico.py        # Gerenciamento de histórico
├── utils/
│   └── validacoes.py       # Validações de dados
└── data/
    ├── compras.json        # Banco de dados de compras
    └── categorias_produtos.json
```

## 📡 API Endpoints

### GET `/api/compras`
Retorna todas as compras registradas
```json
{
  "success": true,
  "compras": [...]
}
```

### POST `/api/compras`
Cria uma nova compra
```json
{
  "mercado": "Carrefour",
  "data": "2026-04-10",
  "hora": "14:30",
  "itens": [
    {
      "produto": "Arroz",
      "preco_unitario": 5.50,
      "quantidade": 2,
      "categoria": "Mercearia"
    }
  ]
}
```

### GET `/api/dashboard`
Retorna estatísticas do dashboard
```json
{
  "success": true,
  "dashboard": {
    "total_compras": 10,
    "total_gasto": 1500.00,
    "media_ticket": 150.00,
    "gasto_por_categoria": {...}
  }
}
```

## 🔐 Segurança

- CORS habilitado para requisições locais
- Validação de dados em cliente e servidor
- Sem armazenamento de dados sensíveis
- Dados persistidos em JSON local

## 🎯 Detecção Automática de Categorias

A aplicação detecta automaticamente a categoria baseada em palavras-chave:

- **Bebidas**: refrigerante, suco, cerveja, água, vinho
- **Mercearia**: arroz, feijão, açúcar, sal, óleo
- **Hortifruti**: alface, tomate, banana, maçã, laranja
- **Carne/Açougue**: carne, frango, peixe
- **Padaria**: pão, bolo, torta
- E mais 18 categorias...

## 📊 Visualização de Dados

### Gráficos Disponíveis

1. **Gasto por Categoria** (Bar Chart)
   - Mostra o valor total gasto em cada categoria
   - Ordena pela maior despesa

2. **Evolução de Compras** (Line Chart)
   - Visualiza a tendência de valores das compras
   - Mostra picos e vales

3. **Distribuição por Categoria** (Doughnut Chart)
   - Percentual de gasto em cada categoria
   - Legenda interativa

## 💡 Dicas de Uso

✅ **Dica 1**: A categoria é detectada automaticamente. Continue digitando o produto e veja a categoria ser preenchida.

✅ **Dica 2**: Use a seção "Comparar" para acompanhar a variação de preços entre compras.

✅ **Dica 3**: O dashboard atualiza automaticamente a cada 5 segundos - não precisa atualizar a página!

✅ **Dica 4**: Clique em uma compra no histórico para ver todos os itens e categorias.

✅ **Dica 5**: Use a análise para identificar em quais categorias você gasta mais.

## 🐛 Troubleshooting

### A aplicação não conecta ao servidor
- Certifique-se de que o servidor Flask está rodando (`python app.py`)
- Verifique se está na porta 5000
- Tente abrir `http://localhost:5000` no navegador

### Os dados não sincronizam
- Verifique a aba "Network" (F12) para ver as requisições
- Confirme que CORS está habilitado no Flask
- Recharge a página (Ctrl+F5)

### Categorias não são detectadas
- Algumas palavras-chave podem estar faltando
- Você pode selecionar manualmente a categoria
- Contribua  adicionando novas palavras-chave!

## 📈 Roadmap Futuro

- [ ] Autenticação de usuários
- [ ] Sincronização em nuvem (Firebase)
- [ ] Exportar relatórios em PDF
- [ ] Modo dark/light
- [ ] Gráficos com mais interatividade
- [ ] Alertas de gastos excessivos
- [ ] Metas de orçamento por categoria
- [ ] App mobile nativo

## 👨‍💻 Desenvolvimento

### Tecnologias Utilizadas
- **Frontend**: HTML5, CSS3, JavaScript Vanilla
- **Backend**: Python, Flask
- **Banco de Dados**: JSON local
- **Gráficos**: Chart.js
- **Ícones**: Font Awesome 6
- **API**: REST com CORS

### Estrutura de Código
- Modular e bem documentado
- Separação clara entre frontend e backend
- Services para lógica de negócio
- Models para estrutura de dados

## 📄 Licença

Este projeto é de código aberto e está disponível para uso pessoal e educacional.

## 👥 Suporte

Dúvidas ou sugestões? Entre em contato para melhorias e novas funcionalidades!

---

**Smart Market v1.0** - Desenvolvido com ❤️ para melhorar sua gestão financeira

© 2026 - Controle suas compras com inteligência
