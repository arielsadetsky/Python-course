from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
from bson import objectid

try:
    con = MongoClient()
    db = con['projeto']
except Exception as e:
    print('Erro: {}'.format(e))

db.usuarios.remove({"_id":1})
db.usuarios.update({"_id":1},{"$set":{"sobrenome":"prata"}})

date = {
    "_id":1,
    'nome':'daniel',
    'sobrenome':'prata',
    'hora':datetime.now().strftime('%d-%m-%y %H:%M:%S')

}
db.usuarios.insert(date)
#usuarios = []
#or usuario in db.usuarios.find():
    #usuarios.append(usuario)

#pprint(usuarios)

usuarios = [x for x in db.usuarios.find()]

b.usuarios.remove({"_id":objectId})
