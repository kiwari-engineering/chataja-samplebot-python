# import unirest
from app.model import Model
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
            Controller.qismeResponse = request.json
            log = open("log-comment.txt", "w")
            log.write(simplejson.dumps(Controller.qismeResponse, indent=4, sort_keys=True))
            log.close()
        else:
            abort(400)

    def run():
        Controller.getResponse() 
        data = Model(
            Controller.qismeResponse["chat_room"]["qiscus_room_id"],
            Controller.qismeResponse["message"]["text"],
            Controller.qismeResponse["message"]["type"],
            Controller.qismeResponse["from"]["fullname"]
        ) 
        print(data.room_id)
        return jsonify({"status":"success"}), 200          