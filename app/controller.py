import simplejson
import urllib3
from app.model import Model
from flask import request, jsonify, abort
from array import *

class Controller:
    access_token = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0Njk1NSwidGltZXN0YW1wIjoiMjAxOS0wNC0wNSAwNjoxMjo0MSArMDAwMCJ9.u5PHjfNPrRL_nhh5S-UUSNLBr2kKBlBI89px2L2jjdg"
    apiurl = "https://qisme.qiscus.com/api/v1/chat/conversations/post_comment"
    headers = {"Accept" : "application/json"} 
    qismeResponse = ""
    http = urllib3.PoolManager()

    def getResponse():
        if request.method == "POST":
            Controller.qismeResponse = request.json
            log = open("log-comment.txt", "w")
            log.write(simplejson.dumps(Controller.qismeResponse, indent=4, sort_keys=True))
            log.close()
        else:
            abort(400)

    #contoh penggunaan api post-comment untuk jenis text
    def replyCommandText(display_name, message_type, room_id):
        comment = "Maaf {}, command yang kamu ketik salah. Jenis pesan kamu adalah {}. Silahkan coba command berikut : /location, /button, /card, /carousel".format(display_name,message_type)

        replay = { 
            "access_token" : Controller.access_token,
            "topic_id" : room_id,
            "type" : "text",
            "comment" : comment 
        }
        text = Controller.http.request("POST", Controller.apiurl, headers=Controller.headers, fields=replay)
        if text.status == 200:
            return jsonify({"status":"success"}), text.status
        else:
            return jsonify({"status":"error"}), text.status   

    def run():
        Controller.getResponse() 
        data = Model(
            Controller.qismeResponse["chat_room"]["qiscus_room_id"],
            Controller.qismeResponse["message"]["text"],
            Controller.qismeResponse["message"]["type"],
            Controller.qismeResponse["from"]["fullname"]
        ) 
        return Controller.replyCommandText(data.sender, data.message_type, data.room_id)
        # return jsonify({"status":"success"}), 200          