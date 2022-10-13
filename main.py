from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)

@app.route("/test-G41/<string:cedula>",methods=['GET'])
def testMethidGetConsulta(cedula):
    variableRespuesta ={
        "respuesta":"Cedula",
        "cedula": cedula
    }
    return variableRespuesta

@app.route("/test-G41",methods=['GET'])
def testMethidGet():
    variableRespuesta ={
        "respuesta":"Test"
    }
    return variableRespuesta

@app.route("/test-G41",methods=['POST'])
def testMethidPost():
    return {
        "respuesta":"POST"
    }

@app.route("/test-G41",methods=['PUT'])
def testMethidPut():
    variableRespuesta ={
        "respuesta":"PUT"
    }
    return variableRespuesta
@app.route("/test-G41",methods=['DELETE'])
def testMethidDelete():
    variableRespuesta ={
        "respuesta":"DELETE"
    }
    return variableRespuesta



def loadFileConfig():
    with open('config.json') as f:
         data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])