from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello World!</h1>'


@app.route('/usuario', methods=['GET'])
def buscar_usuario():
    usuario = {
        "nome": "Renan",
        "idade": 40,
        "telefone": "(19) 988446677"
    }
    return usuario


@app.route('/produto', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    print(f'Novo produto: {dados}')

    return jsonify({'message:': 'Produto cadastrado com sucesso!',
                    "Produto_cadastrado": dados}), 201


@app.route('/produtos', methods=['PUT'])
def atualizar_produto():
    produto = {
        "id": 1,
        "nome": "Caneta Azul",
        "preco": 2.5,
        "descricao": "Caneta esferoráfica",
        "marca": "Bic"
    }

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    if dados['id'] == produto['id']:
        dados == produto

    print(f'Produto atualizado: {produto}')

    return jsonify({'message:': 'Produto atualizado com sucesso!',
                    "Produto_atualizado": produto}), 201
else:
    return jsonify({"message": Produto não encontrado!}), 404


if __name__ == '__main__':
    app.run(debug=True)
