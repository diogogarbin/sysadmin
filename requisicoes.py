#!/usr/bin/python3

import requests
#import json

#response = requests.get('http://127.0.0.1:5000/usuarios')
#response = requests.get('http://phpypesh.com.br')
#print(response.content)
#print(response.json())
#headers = {'Content-Type' : 'application/json '}
#data = json.dumps({"nome" : "João" , "email" : "disjds@kfolks"})
data = {"nome" : "Pero"}
#response = requests.post('http://127.0.0.1:5000/usuarios' , headers=headers, data=data)
response = requests.put('http://127.0.0.1:5000/usuarios/7' , json=data)
print(response.json())
