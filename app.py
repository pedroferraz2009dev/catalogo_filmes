from flask import Flask, request, jsonify, render_template
from psycopg2.extras import RealDictCursor

from database import criar_conexao

app = Flask(__name__)

@app.route('/')
def listar_fimes():
    conn = criar_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM filmes")
    resposta = cursor.fetchall()

    conn.close()

    return render_template("index.html", filmes=resposta)


@app.route('/filme', methods=['POST'])
def cadastrar_filme():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    print(f'Novo filme: {dados}')

    conn = criar_conexao()
    cursor = conn.cursor()

    cursor.execute(
        '''
            INSERT INTO filmes (usuario_id, titulo, ano_lancamento, genero,
            nota, capa_url)
            VALUES (%s, %s, %s, %s, %s, %s)
             RETURNING id
        ''',
        (dados['usuario_id'], dados['titulo'], dados['ano_lancamento'], dados['genero'],
         dados['nota'], dados['capa_url'])
    )

    novo_id = cursor.fetchone()[0]
    conn.commit()

    conn.close()

    return jsonify(
        {
            "messagem": "Filme salvo com sucesso",
            "filme_id": novo_id
         }
    ), 201


@app.route('/produto', methods=['PUT'])
def atualizar_produto():
    produto = {
        "id": 1,
        "nome": "Caneta Vermelha",
        "preco": 1.5,
        "descricao": "Caneta esferográfica",
        "marca": "Bic"
    }

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    if dados["id"] == produto["id"]:
        produto = dados
        print(f'roduto Atualizado {produto}')
        return jsonify({"messagem": "Produto atualizado com sucesso"}), 201
    else:
        return jsonify({"message": "Produto não encontrado"}), 400


@app.route('/teste/db', methods=['GET'])
def testar_conexao():
    conn = criar_conexao()
    print('Testando conexão: ', conn)
    conn.close()
    return jsonify({"message": "Banco conectado com sucesso"}), 200




if __name__ == '__main__':
    app.run(debug=True)
