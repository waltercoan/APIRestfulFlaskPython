from flask import Flask, jsonify, request
from client import Client
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = \
    "mongodb://172.18.0.35:27017/DBwaltercoan"
mongo = PyMongo(app)

#listClients =[
#    Client(name="Zezinho", email="ze@univille.br", phone="5551234"),
#    Client(name="Luizinho", email="lu@univille.br", phone="5555432"),
#    Client(name="Huguinho", email="hu@univille.br", phone="5556666"),
#]

@app.route('/api/v1.0/clients', methods=['GET'])
def get_tasks():
    clients = []
    for c in mongo.db.clients.find():
        newClient = Client()
        newClient._id = str(c['_id'])
        newClient.name = c['name']
        newClient.phone = c['phone']
        newClient.email = c['email']
        clients.append(newClient)
    return jsonify({'clients': \
        [c.__dict__ for c in clients]}), 201
    #return jsonify({'clients':[umcli.__dict__ for umcli in listClients]})

@app.route('/api/v1.0/clients', methods=['POST'])
def create_client():
    newcli = Client()
    newcli._id = ObjectId()
    newcli.name = request.json['name']
    newcli.email = request.json['email']
    newcli.phone = request.json['phone']

    ret = mongo.db.clients.\
        insert_one(newcli.__dict__).inserted_id
    return jsonify({'id': str(ret)}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)







