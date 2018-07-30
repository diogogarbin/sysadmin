import json
from config.mongo import db
from flask import Blueprint, jsonify, make_response
from bson.json_util import dumps as bdumps

usuario = Blueprint('usuarios' , __name__)

@usuario.route('/usuarios')
def usuario_c():
    if request.method == 'GET':
        return jsonify([json.loads(bdumps(u)) for u in db.usuarios.find()])
    else:
        usuario = request.get_json()
        if 'nome' not in usuario.keys() or not usuario['nome'].strip():
            return make_response(jsonify({'message' : 'Propriedade nome Obrigadotória'}), 400) 
        db.usuario.insert(usuario))
        return jsonify({'message : Usuario cadastrado com sucesso'})
