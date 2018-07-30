#!/usr/bin/python3

import requests

response = requests.get('http://localhost:5000/usuarios')
data = response.json()
print ('{0:>10}{1:>30}' .format('ID' , 'NOME'))
for bunda in data['usuarios']:
    if bunda['id'] % 2 == 0 :
        print('{0:.>10}{1:.>30}'.format(bunda['id'], bunda['nome']))
    
    

#print(response.json())
