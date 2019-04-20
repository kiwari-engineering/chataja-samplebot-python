# import unirest
# import model
import simplejson
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
            log = open("log-comment.txt", "w")
            log.write(simplejson.dumps(qismeResponse, indent=4, sort_keys=True))
            log.close()
            return jsonify({"status":"success"}), 200
        else:
            abort(400)

    def run():
        return Controller.getResponse()  
              