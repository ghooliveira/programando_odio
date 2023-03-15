#CRIANDO PR
#CHAMDAS NECESSARIAS PARA CRIAÇÃO DA API
import psycopg2
from flask import Flask, make_response, jsonify, request

#CONEXÇÃO COM O BANCO DE DADOS
mydb = psycopg2.connect(
    host='localhost',
    port='5432',
    user='postgres',
    password='postgres',
    database='postgres',
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#METODO GET QUE RETORNA OS USUARIOS CADASTRADOS NO BANCO

@app.route('/usuarios', methods=['GET'])
def get_usuarios():

    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM tbl_usuarios')
    meus_usuarios = my_cursor.fetchall()

    usuarios = list()
    for usuario in meus_usuarios:
        usuarios.append(
            {
                'id': usuario[0],
                'email': usuario[1],
                'apelido': usuario[2],
                'senha': usuario[3],
            }
        )

    return make_response(
        jsonify(
            message='Lista de usuarios',
            data=usuarios
        )
    )

#METODO POST QUE CADASTRAS OS USUARIOS NO BANCO DE DADOS

@app.route('/usuarios', methods=['POST'])
def create_usuarios():
    usuario = request.json

    my_cursor = mydb.cursor()
    sql = f"INSERT INTO tbl_usuarios (id, email, apelido, senha) VALUES ('{usuario['id']}', '{usuario['email']}', '{usuario['apelido']}', '{usuario['senha']}')"
    my_cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
            message='USUARIO CADASTRADO COM SUCESSO',
            data=usuario
        )
    )

app.run()
