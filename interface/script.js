const API_BASE = "http://localhost:5000/api";
const SYNC_INTERVAL = 5000;

let syncIntervalId = null;
let comprasCache = [];

const CATEGORIAS_VALIDAS = [
    "Mercearia",
    "Massas",
    "Açougue",
    "Frios e Laticinios",
    "Padaria",
    "Hortifruti",
    "Congelados",
    "Doces e Bolachas",
    "Snacks",
    "Bebidas",
    "Temperos e Condimentos",
    "Matinais",
    "Limpeza",
    "Higiene Pessoal",
    "Bebe e Infantil",
    "Pet",
    "Descartaveis",
    "Bazar",
    "Automotivo",
    "Casa e Cozinha",
    "Eletronicos",
    "Saudaveis e Naturais",
    "Outros"
];

const PALAVRAS_CHAVE = {
    "Frios e Laticinios": ["leite", "queijo", "iogurte", "manteiga", "requeijao", "creme", "lacteo"],
    "Açougue": ["carne", "frango", "peixe", "bife", "costela", "linguica", "salsicha"],
    "Mercearia": ["arroz", "feijao", "acucar", "sal", "oleo", "farinha", "trigo", "milho"],
    "Massas": ["macarrao", "massa", "espaguete", "penne", "talharim", "lasanha"],
    "Hortifruti": ["alface", "tomate", "banana", "maca", "laranja", "uva", "batata", "cebola", "alho"],
    "Padaria": ["pao", "bolo", "torta", "croissant", "bisnaga", "pao de forma"],
    "Congelados": ["sorvete", "pizza", "hamburguer", "nugget", "lasanha", "batata frita"],
    "Doces e Bolachas": ["chocolate", "biscoito", "doce", "bolacha", "bala", "caramelo"],
    "Snacks": ["chips", "salgadinho", "pipoca", "amendoim"],
    "Bebidas": ["refrigerante", "suco", "cerveja", "agua", "vinho", "whisky", "coca", "cola", "fanta", "pepsi", "guarana", "refri"],
    "Temperos e Condimentos": ["azeite", "vinagre", "mostarda", "ketchup", "pimenta", "molho"],
    "Matinais": ["cereal", "granola", "aveia", "cafe", "cha", "sucrilhos", "nescau cereal"],
    "Limpeza": ["sabao", "detergente", "desinfetante", "esponja", "amaciante", "limpa"],
    "Higiene Pessoal": ["shampoo", "sabonete", "desodorante", "creme dental", "absorvente"],
    "Bebe e Infantil": ["fralda", "papinha", "mamadeira", "chupeta", "leite em po"],
    "Pet": ["racao", "areia", "coleira"],
    "Descartaveis": ["guardanapo", "papel toalha", "prato descartavel", "copos descartaveis"],
    "Casa e Cozinha": ["panela", "prato", "copo", "utensilio", "eletrodomestico"],
    "Automotivo": ["oleo motor", "acessorio automotivo"],
    "Eletronicos": ["lampada", "bateria", "carregador", "fone de ouvido"],
    "Saudaveis e Naturais": ["organico", "integral", "sem gluten", "natural", "vegano"]
};

const chartInstances = {
    categoria: null,
    comparacao: null,
    participacao: null
};

function formatCurrency(value) {
    return new Intl.NumberFormat("pt-BR", {
        style: "currency",
        currency: "BRL"
    }).format(Number(value || 0));
}

function normalizarTexto(texto) {
    if (!texto) return "";
    return texto
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toLowerCase()
        .replace(/\s+/g, " ")
        .trim();
}

function obterCategoriaPorPalavraChave(nomeProduto) {
    const produto = normalizarTexto(nomeProduto);
    if (!produto) return "Outros";

    for (const [categoria, palavras] of Object.entries(PALAVRAS_CHAVE)) {
        for (const palavra of palavras) {
            if (produto.includes(normalizarTexto(palavra))) {
                return categoria;
            }
        }
    }

    return "Outros";
}

function showToast(message, type = "success") {
    const toast = document.createElement("div");
    const icon = type === "success" ? "check-circle" : "exclamation-circle";

    toast.className = `toast ${type}`;
    toast.innerHTML = `<i class="fas fa-${icon}"></i><span>${message}</span>`;

    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

function showSection(sectionId, button) {
    document.querySelectorAll("section").forEach(section => {
        section.classList.remove("active");
    });

    document.querySelectorAll(".nav-button").forEach(navButton => {
        navButton.classList.remove("active");
    });

    const section = document.getElementById(sectionId);
    if (section) {
        section.classList.add("active");
    }

    if (button) {
        button.classList.add("active");
    }

    if (sectionId === "dashboard") renderDashboard();
    if (sectionId === "historico") renderHistorico();
    if (sectionId === "comparar") populateComparison();
    if (sectionId === "analisar") renderAnalise();
}

async function fetchCompras() {
    try {
        const response = await fetch(`${API_BASE}/compras`);
        const data = await response.json();

        if (data.success) {
            comprasCache = data.compras || [];
        }

        return comprasCache;
    } catch (error) {
        console.error("Erro ao buscar compras:", error);
        return [];
    }
}

async function startSync() {
    syncIntervalId = setInterval(async () => {
        await fetchCompras();

        if (document.getElementById("dashboard").classList.contains("active")) {
            updateDashboardMetrics();
        }
    }, SYNC_INTERVAL);
}

function stopSync() {
    if (syncIntervalId) {
        clearInterval(syncIntervalId);
    }
}

function addItem() {
    const itensDiv = document.getElementById("itens");
    const itemCount = itensDiv.querySelectorAll(".item").length + 1;

    const itemDiv = document.createElement("div");
    itemDiv.className = "item";
    itemDiv.innerHTML = `
        <div class="item-header">
            <div class="item-number">${itemCount}</div>
            <button type="button" class="btn-remove-item btn-sm" onclick="removeItem(this)">
                <i class="fas fa-trash"></i> Remover
            </button>
        </div>

        <div class="form-group-row">
            <div class="form-group">
                <label><i class="fas fa-tag"></i> Produto</label>
                <input type="text" class="produto" placeholder="Ex: Arroz integral..." required>
            </div>
            <div class="form-group">
                <label><i class="fas fa-folder"></i> Categoria</label>
                <select class="categoria">
                    <option value="">Auto-detectar</option>
                    ${CATEGORIAS_VALIDAS.map(c => `<option value="${c}">${c}</option>`).join("")}
                </select>
            </div>
        </div>

        <div class="form-group-row">
            <div class="form-group">
                <label><i class="fas fa-dollar-sign"></i> Preço Unitário</label>
                <input type="number" step="0.01" class="preco" placeholder="0.00" required>
            </div>
            <div class="form-group">
                <label><i class="fas fa-hashtag"></i> Quantidade</label>
                <input type="number" step="0.01" class="quantidade" placeholder="1" required>
            </div>
        </div>
    `;

    itensDiv.appendChild(itemDiv);

    const produtoInput = itemDiv.querySelector(".produto");
    const categoriaSelect = itemDiv.querySelector(".categoria");

    produtoInput.addEventListener("input", (e) => {
        if (!categoriaSelect.dataset.manual) {
            categoriaSelect.value = obterCategoriaPorPalavraChave(e.target.value);
        }
    });

    categoriaSelect.addEventListener("change", () => {
        categoriaSelect.dataset.manual = categoriaSelect.value ? "true" : "";
    });
}

function removeItem(button) {
    button.closest(".item").remove();

    document.querySelectorAll("#itens .item-number").forEach((el, idx) => {
        el.textContent = idx + 1;
    });
}

document.getElementById("compraForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();

    const mercado = document.getElementById("mercado").value;
    const data = document.getElementById("data").value;
    const hora = document.getElementById("hora").value;

    const itensElements = document.querySelectorAll("#itens .item");
    const itens = Array.from(itensElements).map(item => ({
        produto: item.querySelector(".produto").value,
        preco_unitario: parseFloat(item.querySelector(".preco").value),
        quantidade: parseInt(item.querySelector(".quantidade").value, 10),
        categoria: item.querySelector(".categoria").value || ""
    }));

    if (itens.length === 0) {
        showToast("Adicione pelo menos um item", "error");
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/compras`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ mercado, data, hora, itens })
        });

        const result = await response.json();

        if (result.success) {
            showToast("Compra registrada com sucesso!", "success");
            e.target.reset();
            document.getElementById("itens").innerHTML = "";
            addItem();
            document.getElementById("data").value = new Date().toISOString().split("T")[0];
            await fetchCompras();
            renderDashboard();
        } else {
            showToast(`Erro: ${result.error}`, "error");
        }
    } catch (error) {
        console.error(error);
        showToast("Erro ao salvar compra", "error");
    }
});

function updateDashboardMetrics() {
    const compras = comprasCache;

    if (compras.length === 0) {
        document.getElementById("totalCompras").textContent = "0";
        document.getElementById("totalGasto").textContent = "R$ 0,00";
        document.getElementById("mediaTicket").textContent = "R$ 0,00";
        document.getElementById("topCategoria").textContent = "—";
        return;
    }

    const totalCompras = compras.length;
    const totalGasto = compras.reduce((sum, compra) => sum + (compra.total_compra || 0), 0);
    const mediaTicket = totalGasto / totalCompras;

    const gastoPorCategoria = {};
    compras.forEach(compra => {
        (compra.itens || []).forEach(item => {
            const categoria = item.categoria || "Outros";
            gastoPorCategoria[categoria] = (gastoPorCategoria[categoria] || 0) + (item.total_item || 0);
        });
    });

    const topCategoria = Object.entries(gastoPorCategoria).length > 0
        ? Object.entries(gastoPorCategoria).sort((a, b) => b[1] - a[1])[0][0]
        : "—";

    document.getElementById("totalCompras").textContent = totalCompras;
    document.getElementById("totalGasto").textContent = formatCurrency(totalGasto);
    document.getElementById("mediaTicket").textContent = formatCurrency(mediaTicket);
    document.getElementById("topCategoria").textContent = topCategoria;

    renderCharts(compras);
}

function renderCharts(compras) {
    if (compras.length === 0) return;

    const gastoPorCategoria = {};
    compras.forEach(compra => {
        (compra.itens || []).forEach(item => {
            const categoria = item.categoria || "Outros";
            gastoPorCategoria[categoria] = (gastoPorCategoria[categoria] || 0) + (item.total_item || 0);
        });
    });

    const categorias = Object.keys(gastoPorCategoria);
    const valores = Object.values(gastoPorCategoria);
    const cores = ["#10b981", "#3b82f6", "#f59e0b", "#ef4444", "#8b5cf6", "#06b6d4", "#ec4899", "#f97316"];

    const ctx1 = document.getElementById("categoriaChart")?.getContext("2d");
    if (ctx1) {
        if (chartInstances.categoria) chartInstances.categoria.destroy();

        chartInstances.categoria = new Chart(ctx1, {
            type: "bar",
            data: {
                labels: categorias,
                datasets: [{
                    label: "Gasto por Categoria",
                    data: valores,
                    backgroundColor: cores,
                    borderRadius: 8,
                    maxBarThickness: 50
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: { grid: { display: false } },
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: value => formatCurrency(value)
                        }
                    }
                }
            }
        });
    }

    const ctx2 = document.getElementById("comparacaoChart")?.getContext("2d");
    if (ctx2) {
        if (chartInstances.comparacao) chartInstances.comparacao.destroy();

        const labels = compras.map((_, i) => `Compra ${i + 1}`);
        const valoresCompras = compras.map(compra => compra.total_compra || 0);

        chartInstances.comparacao = new Chart(ctx2, {
            type: "line",
            data: {
                labels,
                datasets: [{
                    label: "Valor da Compra",
                    data: valoresCompras,
                    borderColor: "#10b981",
                    backgroundColor: "rgba(16, 185, 129, 0.1)",
                    fill: true,
                    tension: 0.35,
                    pointRadius: 5,
                    pointBackgroundColor: "#10b981",
                    pointBorderColor: "#fff",
                    pointBorderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: value => formatCurrency(value)
                        }
                    }
                }
            }
        });
    }

    const ctx3 = document.getElementById("participacaoChart")?.getContext("2d");
    if (ctx3) {
        if (chartInstances.participacao) chartInstances.participacao.destroy();

        chartInstances.participacao = new Chart(ctx3, {
            type: "doughnut",
            data: {
                labels: categorias,
                datasets: [{
                    data: valores,
                    backgroundColor: cores,
                    borderColor: "#fff",
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: "bottom" }
                }
            }
        });
    }
}

function renderDashboard() {
    updateDashboardMetrics();
}

function renderHistorico() {
    const container = document.getElementById("historicoContainer");
    const compras = comprasCache;

    if (compras.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-inbox"></i>
                <p>Nenhuma compra registrada ainda</p>
            </div>
        `;
        return;
    }

    container.innerHTML = `
        <ul class="list-container">
            ${compras.map((compra, idx) => `
                <li class="list-item" onclick="showCompraDetail(${idx})">
                    <div>
                        <div class="list-item-title">
                            <i class="fas fa-store"></i> ${compra.mercado}
                            <span style="opacity: 0.7; margin-left: 0.5rem;">
                                ${compra.data} às ${compra.hora}
                            </span>
                        </div>
                        <small style="color: #999;">
                            ${compra.total_itens || 0} item(s) •
                            ${(compra.itens || [])
                                .map(item => item.categoria)
                                .filter((valor, i, arr) => valor && arr.indexOf(valor) === i)
                                .join(", ")}
                        </small>
                    </div>
                    <div class="list-item-value">${formatCurrency(compra.total_compra || 0)}</div>
                </li>
            `).join("")}
        </ul>
    `;
}

function showCompraDetail(idx) {
    const compra = comprasCache[idx];
    if (!compra) return;

    alert(`
DETALHES DA COMPRA
==================
Mercado: ${compra.mercado}
Data: ${compra.data}
Hora: ${compra.hora}
Total: ${formatCurrency(compra.total_compra || 0)}
Itens: ${compra.total_itens || 0}

ITENS:
${(compra.itens || [])
    .map(item => `- ${item.produto} (${item.categoria || "Outros"}): ${formatCurrency(item.total_item || 0)}`)
    .join("\n")}
    `.trim());
}

function populateComparison() {
    const compras = comprasCache;
    const options = compras.map((compra, i) =>
        `<option value="${i}">${compra.mercado} - ${compra.data} - ${formatCurrency(compra.total_compra || 0)}</option>`
    ).join("");

    document.getElementById("compra1").innerHTML = `<option value="">Selecione uma compra</option>${options}`;
    document.getElementById("compra2").innerHTML = `<option value="">Selecione uma compra</option>${options}`;
}

function compararCompras() {
    const idx1 = parseInt(document.getElementById("compra1").value, 10);
    const idx2 = parseInt(document.getElementById("compra2").value, 10);

    if (isNaN(idx1) || isNaN(idx2)) {
        showToast("Selecione duas compras", "error");
        return;
    }

    const compra1 = comprasCache[idx1];
    const compra2 = comprasCache[idx2];

    if (!compra1 || !compra2) {
        showToast("Compras não encontradas", "error");
        return;
    }

    const diferenca = (compra2.total_compra || 0) - (compra1.total_compra || 0);
    const percentualDif = compra1.total_compra
        ? (diferenca / compra1.total_compra) * 100
        : 0;

    const resultado = document.getElementById("resultadoComparacao");

    resultado.innerHTML = `
        <div class="comparison-box">
            <div class="comparison-item">
                <h3><i class="fas fa-receipt"></i> ${compra1.mercado}</h3>
                <div class="difference"><span class="difference-label">Data</span><span>${compra1.data} ${compra1.hora}</span></div>
                <div class="difference"><span class="difference-label">Total</span><span class="difference-value">${formatCurrency(compra1.total_compra || 0)}</span></div>
                <div class="difference"><span class="difference-label">Itens</span><span>${compra1.total_itens || 0}</span></div>
            </div>

            <div class="comparison-item">
                <h3><i class="fas fa-receipt"></i> ${compra2.mercado}</h3>
                <div class="difference"><span class="difference-label">Data</span><span>${compra2.data} ${compra2.hora}</span></div>
                <div class="difference"><span class="difference-label">Total</span><span class="difference-value">${formatCurrency(compra2.total_compra || 0)}</span></div>
                <div class="difference"><span class="difference-label">Itens</span><span>${compra2.total_itens || 0}</span></div>
            </div>
        </div>

        <div class="card">
            <h3><i class="fas fa-chart-line"></i> Análise da Diferença</h3>
            <div class="difference">
                <span class="difference-label">Diferença</span>
                <span class="difference-value" style="color: ${diferenca > 0 ? "#ef4444" : "#10b981"}">
                    ${formatCurrency(Math.abs(diferenca))} ${diferenca > 0 ? "(+)" : "(-)"}
                </span>
            </div>
            <div class="difference">
                <span class="difference-label">Percentual</span>
                <span style="color: ${percentualDif > 0 ? "#ef4444" : "#10b981"}">
                    ${percentualDif > 0 ? "+" : ""}${percentualDif.toFixed(2)}%
                </span>
            </div>
        </div>
    `;
}

function renderAnalise() {
    const compras = comprasCache;
    const container = document.getElementById("analiseContainer");

    if (compras.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-chart-pie"></i>
                <p>Sem dados para análise</p>
            </div>
        `;
        return;
    }

    const gastoPorCategoria = {};
    compras.forEach(compra => {
        (compra.itens || []).forEach(item => {
            const categoria = item.categoria || "Outros";
            gastoPorCategoria[categoria] = (gastoPorCategoria[categoria] || 0) + (item.total_item || 0);
        });
    });

    const topCategorias = Object.entries(gastoPorCategoria)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10);

    const totalGasto = Object.values(gastoPorCategoria).reduce((a, b) => a + b, 0);

    container.innerHTML = `
        <ul class="list-container">
            ${topCategorias.map(([categoria, valor], idx) => {
                const percentual = totalGasto ? (valor / totalGasto) * 100 : 0;

                return `
                    <li class="list-item">
                        <div style="flex: 1;">
                            <div class="list-item-title">
                                <span style="margin-right: 1rem; font-weight: 700; color: #10b981;">#${idx + 1}</span>
                                ${categoria}
                            </div>
                            <div style="margin-top: 0.5rem;">
                                <div style="background: #f3f4f6; height: 8px; border-radius: 4px; overflow: hidden;">
                                    <div style="background: linear-gradient(90deg, #10b981, #3b82f6); height: 100%; width: ${percentual}%;"></div>
                                </div>
                                <small style="color: #999; margin-top: 0.25rem; display: block;">
                                    ${percentual.toFixed(1)}% do total
                                </small>
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <div class="list-item-value" style="margin-bottom: 0.25rem;">${formatCurrency(valor)}</div>
                            <small style="color: #999;">${formatCurrency(valor / compras.length)}/compra</small>
                        </div>
                    </li>
                `;
            }).join("")}
        </ul>
    `;
}

document.addEventListener("DOMContentLoaded", async () => {
    if (document.getElementById("itens").children.length === 0) {
        addItem();
    }

    document.getElementById("data").value = new Date().toISOString().split("T")[0];

    await fetchCompras();
    renderDashboard();
    startSync();
});

window.addEventListener("beforeunload", stopSync);