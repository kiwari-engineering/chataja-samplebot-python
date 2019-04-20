# import unirest
# import model
from flask import request, jsonify, abort
from array import *

class Controller:
    access_token = ""
    apiurl = "https://qisme.qiscus.com/api/v1/chat/conversations/"
    headers = {"Content-Type" : "application/json"} 
    qismeResponse = ""

    def getResponse():
        if request.method == "POST":
            qismeResponse = request.json
            print(qismeResponse)
            return '', 200
        else:
            abort(400)

    def run():
        return Controller.getResponse()  
              