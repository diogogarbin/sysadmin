#!/usr/bin/python3

from flask import Blueprint, Flask, jsonify, request, make_response, json, render_template
from datetime import datetime
app = Flask(__name__)
from config.mongo import db
from bson.json_util import dumps as bdumps
import blueprints.jk imports jk

from blueprints.usuario import usuario
app.register_blueprint(usuario)
def contador():
    contador = 0
    with open('contador' , 'r') as f:
        contador = f.read()
        if contador == '':
            contador = 1
        else:
            contador = int(contador) + 1
    with open('contador' , 'w') as f:
        f.write(str(contador))
    return contador
 
@app.route('/')
def home():
    c = contador()
    print('teste')
    return render_template('index.html', title='Home')


#Criar uma rota chamada "acessos" que retorna um json contendo a data atual e um contador que terá o valor (por enquanto) 
#{'date' : '2018-07-13', 'count' 0}

@app.route('/acessos')
def acessos():
    date = datetime.now().strftime('%Y-%m-%d %H:%I:%S')
    return jsonify({'date' : date, 'count' : 0})

@app.route('/celular' , methods=['POST' ,' GET'])
def celular():
#    return jsonify(request.get_json())
    retorno = json.dumps({'status' : 'Não encontrado'})
    headers = {'Content-Type' : 'application/json'}
    return make_response(retorno, 404, headers)


@app.route('/usr_banco')
def usr_banco():
    return jsonify([json.loads(bdumps(u)) for u in db.usuarios.find()])
app.run(host='0.0.0.0' , port=65000)

#Toda vez que uma rota for acessada, abrir um arquivo de texto e incrementar +1 no valor do arquivo quando acessar a rota /acessos retornar este valor em count


