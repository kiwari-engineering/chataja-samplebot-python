import unirest
from model import *
from flask import request, jsonify, abort
from array import *

class Controller:

    def __init__(self):
        self.access_token = ""
        self.apiurl = "https://qisme.qiscus.com/api/v1/chat/conversations/"
        self.headers = {"Content-Type" : "application/json"} 
        self.qismeResponse = ""

    def getResponse():
        if request.method == "POST":
            self.qismeResponse = request.json
            print(self.qismeResponse)
            return '', 200
        else:
            abort(400)

    def run():
        self.getResponse()        