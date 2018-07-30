#!/usr/bin/python3

from flask import Flask, jsonify, request, make_response, json
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    print('teste')
    return jsonify({'status' : 'Running ...'})

from blueprints.usuario import usuario
app.register_blueprint(usuario)
