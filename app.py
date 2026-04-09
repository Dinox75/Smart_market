# ==========================================
# 📦 ARQUIVO: app.py
# 🎯 RESPONSABILIDADE:
# Servidor web Flask para integrar frontend com backend
# Fornece API REST e serve interface web
# ==========================================

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
from services.historico import carregar_compras, salvar_compra
from services.comparacoes import comparar_compras
from services.categorizar import obter_categoria_produto
import json
from datetime import datetime

app = Flask(__name__, template_folder='.')
CORS(app)

# ==========================================
# 🌐 ROTAS WEB
# ==========================================

@app.route('/')
def index():
    """Serve a página principal"""
    return render_template('index.html')

# ==========================================
# 🔌 API ENDPOINTS
# ==========================================

@app.route('/api/compras', methods=['GET'])
def get_compras():
    """Retorna todas as compras"""
    try:
        compras = carregar_compras()
        return jsonify({'success': True, 'compras': compras})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/compras', methods=['POST'])
def create_compra():
    """Cria uma nova compra"""
    try:
        data = request.get_json()

        # Validar dados básicos
        mercado = validar_mercado(data.get('mercado'))
        data_compra = validar_data(data.get('data'))
        hora = validar_hora(data.get('hora'))

        compra = Compra(mercado, data_compra, hora)

        # Processar itens
        for item_data in data.get('itens', []):
            produto = validar_produto(item_data.get('produto'))
            categoria = obter_categoria_produto(produto)
            quantidade = validar_quantidade(item_data.get('quantidade'))
            preco = validar_preco(item_data.get('preco_unitario'))

            item = Item(produto, preco, quantidade, categoria)
            compra.adicionar_item(item)

        # Salvar compra
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
    """Retorna uma compra específica"""
    try:
        compras = carregar_compras()
        if 0 <= compra_id < len(compras):
            return jsonify({'success': True, 'compra': compras[compra_id]})
        return jsonify({'success': False, 'error': 'Compra não encontrada'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/comparar', methods=['POST'])
def comparar():
    """Compara duas compras"""
    try:
        data = request.get_json()
        compra1_id = data.get('compra1_id')
        compra2_id = data.get('compra2_id')

        compras = carregar_compras()
        if not (0 <= compra1_id < len(compras) and 0 <= compra2_id < len(compras)):
            return jsonify({'success': False, 'error': 'IDs de compra inválidos'}), 400

        compra1 = compras[compra1_id]
        compra2 = compras[compra2_id]

        resultado = comparar_compras(compra2, compra1)

        return jsonify({'success': True, 'comparacao': resultado})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    """Retorna dados para o dashboard"""
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

        # Cálculos básicos
        total_compras = len(compras)
        total_gasto = sum(c['total_compra'] for c in compras)
        media_ticket = total_gasto / total_compras if total_compras > 0 else 0

        # Gasto por categoria
        gasto_categoria = {}
        for compra in compras:
            for item in compra['itens']:
                cat = item.get('categoria', 'Outros')
                gasto_categoria[cat] = gasto_categoria.get(cat, 0) + item['total_item']

        top_categoria = max(gasto_categoria.items(), key=lambda x: x[1])[0] if gasto_categoria else None

        # Histórico de valores
        historico_valores = [c['total_compra'] for c in compras[-10:]]  # Últimas 10

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

@app.route('/api/categorias', methods=['GET'])
def get_categorias():
    """Retorna lista de categorias válidas"""
    from services.categorizar import CATEGORIAS_VALIDAS
    return jsonify({'success': True, 'categorias': CATEGORIAS_VALIDAS})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)