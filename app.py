from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from models.compra import Compra
from models.item import Item

from utils.validacoes import (
    validar_mercado,
    validar_data,
    validar_hora,
    validar_produto,
    validar_quantidade,
    validar_preco
)

from services.categorizar import obter_categoria_produto, CATEGORIAS_VALIDAS, padronizar_nome_produto
from services.historico import carregar_compras, salvar_compra
from services.comparacoes import comparar_compras

app = Flask(__name__, template_folder='interface')
CORS(app)


# ==========================================
# 🌐 FRONTEND
# ==========================================

@app.route('/')
def index():
    return render_template('index.html')


# ==========================================
# 📦 COMPRAS
# ==========================================

@app.route('/api/compras', methods=['GET'])
def get_compras():
    try:
        compras = carregar_compras()
        return jsonify({'success': True, 'compras': compras})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/compras', methods=['POST'])
def create_compra():
    try:
        data = request.get_json()

        # 🔹 VALIDAÇÃO PRINCIPAL
        mercado = validar_mercado(data.get('mercado'))
        data_compra = validar_data(data.get('data'))  # aceita ISO agora
        hora = validar_hora(data.get('hora'))

        compra = Compra(mercado, data_compra, hora)

        # 🔹 ITENS
        itens = data.get('itens', [])

        if not itens:
            return jsonify({'success': False, 'error': 'A compra precisa ter itens'}), 400

        for item_data in itens:
            produto = validar_produto(item_data.get('produto'))
            produto = padronizar_nome_produto(produto)

            quantidade = validar_quantidade(item_data.get('quantidade'))
            preco = validar_preco(item_data.get('preco_unitario'))

            categoria = obter_categoria_produto(produto)

            item = Item(produto, preco, quantidade, categoria)
            compra.adicionar_item(item)

        salvar_compra(compra)

        return jsonify({
            'success': True,
            'compra': compra.to_dict(),
            'message': 'Compra registrada com sucesso!'
        })

    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/compras/<int:compra_id>', methods=['GET'])
def get_compra(compra_id):
    try:
        compras = carregar_compras()

        if 0 <= compra_id < len(compras):
            return jsonify({'success': True, 'compra': compras[compra_id]})

        return jsonify({'success': False, 'error': 'Compra não encontrada'}), 404

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# ==========================================
# 🔍 COMPARAÇÃO
# ==========================================

@app.route('/api/comparar', methods=['POST'])
def comparar():
    try:
        data = request.get_json()

        id1 = data.get('compra1_id')
        id2 = data.get('compra2_id')

        compras = carregar_compras()

        if not isinstance(id1, int) or not isinstance(id2, int):
            return jsonify({'success': False, 'error': 'IDs inválidos'}), 400

        if not (0 <= id1 < len(compras) and 0 <= id2 < len(compras)):
            return jsonify({'success': False, 'error': 'IDs fora do range'}), 400

        resultado = comparar_compras(compras[id2], compras[id1])

        return jsonify({'success': True, 'comparacao': resultado})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# ==========================================
# 📊 DASHBOARD
# ==========================================

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    try:
        compras = carregar_compras()

        if not compras:
            return jsonify({
                'success': True,
                'dashboard': {
                    'total_compras': 0,
                    'total_gasto': 0,
                    'media_ticket': 0,
                    'top_categoria': None,
                    'gasto_por_categoria': {},
                    'historico_valores': []
                }
            })

        total_compras = len(compras)
        total_gasto = round(sum(c['total_compra'] for c in compras), 2)
        media_ticket = round(total_gasto / total_compras, 2)

        gasto_categoria = {}

        for compra in compras:
            for item in compra['itens']:
                cat = item.get('categoria') or 'Outros'
                gasto_categoria[cat] = gasto_categoria.get(cat, 0) + item['total_item']

        # arredondar valores
        gasto_categoria = {k: round(v, 2) for k, v in gasto_categoria.items()}

        top_categoria = max(gasto_categoria.items(), key=lambda x: x[1])[0] if gasto_categoria else None

        historico_valores = [round(c['total_compra'], 2) for c in compras[-10:]]

        return jsonify({
            'success': True,
            'dashboard': {
                'total_compras': total_compras,
                'total_gasto': total_gasto,
                'media_ticket': media_ticket,
                'top_categoria': top_categoria,
                'gasto_por_categoria': gasto_categoria,
                'historico_valores': historico_valores
            }
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# ==========================================
# 📂 CATEGORIAS
# ==========================================

@app.route('/api/categorias', methods=['GET'])
def get_categorias():
    return jsonify({'success': True, 'categorias': CATEGORIAS_VALIDAS})


# ==========================================
# 🚀 RUN
# ==========================================

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)