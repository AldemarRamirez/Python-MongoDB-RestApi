from flask import Flask, jsonify, request, Response
from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS
import json

app = Flask(__name__)

# Permite que cualquier dominio use nuestra API
CORS(app)
# Para permitir un recurso en especifico a cualquier dominio se puede usar lo siguiente
# CORS(app, resources={r'/documento/*'; {'origins'='*'}})

# Coneccion con mongodb Atlas
CONNECTION_STRING = "mongodb+srv://m220student:m220password@cluster0.kdegh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client.melichallenge

# Metodo para subir un documento a la DB 
# En el body de la peticion se recibe un JSON con el titulo y el contenido del archivo
# Retorna 404 de no encontrar las llaves en el JSON o un JSON con el Id correspondiente en la DB
@app.route('/documento', methods=['POST'])
def create_documento():
    # Recomendable recibir el contenido con codificacion utf-8
    titulo = request.json['titulo']
    contenido = request.json['contenido']

    if titulo and contenido:
        id = db.documentos.insert_one({'titulo': titulo, 'contenido': contenido})
        response = jsonify({
            '_id': str(id),
        })
        response.status_code = 201
        return response
    else:
        return not_found()

# Metodo para consultar un documento por el nombre.
# Formato = documento/?doc_name=320-8.txt
# Retorna el id en DB, el titulo y el contenido del documento
@app.route('/documento/', methods=['GET'])
def get_documento():
    doc_name = request.args.get('doc_name')
    documento = db.documentos.find({'titulo': doc_name})
    response = json_util.dumps(documento)
    return Response(response, mimetype="application/json")

# Metodo para consultar una palabra en un documento en especifico o en toda la colleccion 
# Formato = /?doc_name=5985-8.txt&term=casa
# Retorna la cantidad de veces que se encontro la palabra
@app.route('/', methods=['GET'])
def get_consulta():
    doc_name = request.args.get('doc_name')
    term = request.args.get('term')
    dict_docs = []
    valor = 0
    respuesta = {}

    if doc_name and term:
        # Busqueda por una palabra y un documento en especifico
        documento = db.documentos.find({'titulo': doc_name})
        str_docs = json_util.dumps(documento)
        dict_docs = json.loads(str_docs)
    elif term:
        # Busqueda por una palabra en la coleccion de documentos
        documento = db.documentos.find()
        str_docs = json_util.dumps(documento)
        dict_docs = json.loads(str_docs)
    else:
        return not_found()

    for doc in dict_docs:
        valor += doc.get('contenido').count(term)
    respuesta.setdefault('frecuencia', valor)
    
    return Response(json.dumps(respuesta), mimetype="application/json")

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == "__main__":    
    app.run(host="0.0.0.0", port=4000, debug=True)