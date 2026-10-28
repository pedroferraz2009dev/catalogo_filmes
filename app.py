from flask import Flask, request, jsonify, render_template, redirect, url_for
from psycopg2.extras import RealDictCursor

from database import criar_conexao

app = Flask(__name__)

@app.route('/')
def listar_filmes():
    conn = criar_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM filmes")
    resposta = cursor.fetchall()

    conn.close()

    return render_template("index.html", filmes=resposta)

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_filme(id):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM filmes WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("listar_fimes"))

@app.route('/novo', methods=["GET",'POST'])
def novo_filme():
    if request.method == "POST":
        titulo = request.form['titulo']
        genero = request.form['genero']
        capa_url = request.form['capa_url']
        nota = request.form['nota']
        ano_lancamento = request.form['ano_lancamento']
        usuario_id = 1

        parametros = [titulo, genero, capa_url, nota, ano_lancamento, usuario_id]

        sql = '''
        INSERT INTO filmes 
        (titulo, genero, capa_url, nota, ano_lancamento, usuario_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute(sql, parametros)
        conn.commit()
        conn.close()
        return redirect(url_for("listar_filmes"))

    return render_template("novo_filme.html")


@app.route('/teste/db', methods=['GET'])
def testar_conexao():
    conn = criar_conexao()
    print('Testando conexão: ', conn)
    conn.close()
    return jsonify({"message": "Banco conectado com sucesso"}), 200




if __name__ == '__main__':
    app.run(debug=True)
