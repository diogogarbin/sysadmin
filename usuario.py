import json
from config.mongo import db
from flask import Blueprint, jsonify, make_response, Response, render_template, request
from bson.json_util import dumps as bdumps

usuario = Blueprint('usuarios' , __name__)

@usuario.route('/usuarios')
def usuario_c():
    if request.method == 'GET':
        #return Response(bdumps(db.usuarios.find()), content_type='application/json')
        return render_template('index.html', usuarios=db.usuarios.find())
    else:
        usuario = request.get_json()
        if 'nome' not in usuario.keys() or not usuario['nome'].strip():
            return make_response(jsonify({'message' : 'Propriedade nome Obrigadotória'}), 400) 
        db.usuario.insert(usuario)
        return jsonify({'message : Usuario cadastrado com sucesso'})
