import simplejson #panggil library json
import urllib3 #panggil library http request
from app.model import Model #panggil model
from flask import request, jsonify, abort
from array import *

class Controller:
    #set atribut yang dibutuhkan untuk controller
    access_token = "<input akses token disini>"
    apiurl = "https://api.kiwari.chat/api/v1/chat/conversations/post_comment"
    apiResponse = "" #atribut untuk nampung response
    http = urllib3.PoolManager() #inisiasi atribut http request library urllib3

    #ambil dan tampung response data dari webhook
    def getResponse():
        if request.method == "POST":
            Controller.apiResponse = request.json

            #siapkan log untuk memastikan data terambil
            log = open("log-comment.txt", "w")
            log.write(simplejson.dumps(Controller.apiResponse, indent=4, sort_keys=True))
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
        text = Controller.http.request("POST", Controller.apiurl, fields=replay)
        if text.status == 200:
            return jsonify({"status":"success"}), text.status
        else:
            return abort(text.status)   

    #contoh penggunaan api post-comment untuk jenis button
    def replyCommandButton(room_id, display_name):
        comment = "Halo {}, ini adalah contoh payload button yang bisa kamu coba".format(display_name)
        payload = {
            "text" : comment,
            "buttons" : [
                {
                    "label" : "Hitam",
                    "type" : "postback",
                    "postback_text" : "Putih",
                    "payload" : {
                        "url" : "#",
                        "method" : "get",
                        "payload" : None
                    }
                },
                {
                    "label" : "Tombol Link",
                    "type" : "link",
                    "payload" : {
                        "url" : "https://www.kiwari.chat",
                    }
                }
            ]
        }
        encoded_data = simplejson.dumps(payload).encode("utf-8")
        replay = { 
            "access_token" : Controller.access_token,
            "topic_id" : room_id,
            "type" : "buttons",
            "payload" : encoded_data
        }
        buttons = Controller.http.request("POST", Controller.apiurl, fields=replay)
        if buttons.status == 200:
            return jsonify({"status":"success"}), buttons.status
        else:
            return jsonify({"status":"error"}), buttons.status  

    #contoh penggunaan api post-comment untuk jenis location
    def replyCommandLocation(room_id):
        payload = {
            "name" : "Telkom Landmark Tower",
            "address" : "Jalan Jenderal Gatot Subroto No.Kav. 52, West Kuningan, Mampang Prapatan, South Jakarta City, Jakarta 12710",
            "latitude" : "-6.2303817",
            "longitude" : "106.8159363",
            "map_url" : "https://www.google.com/maps/@-6.2303817,106.8159363,17z"
        }
        encoded_data = simplejson.dumps(payload).encode("utf-8")
        replay = {
            "access_token" : Controller.access_token,
            "topic_id" : room_id,
            "type" : "location",
            "payload" : encoded_data
        }
        location  = Controller.http.request("POST", Controller.apiurl, fields=replay)
        if location.status == 200:
            return jsonify({"status":"success"}), location.status
        else:
            return jsonify({"status":"error"}), location.status 
    
    #contoh penggunaan api post-comment untuk jenis carousel
    def replyCommandCarousel(room_id):
        payload = {
            "cards" : [
                {
                    "image" : "https://cdns.img.com/a.jpg",
                    "title" : "Gambar 1",
                    "description" : "Carousel Double Button",
                    "default_action" : {
                        "type" : "postback",
                        "postback_text" : "Load More...",
                        "payload" : {
                            "url" : "https://j.id",
                            "method" : "GET",
                            "payload": None
                        }
                    },
                    "buttons" : [
                        {
                            "label" : "Button 1",
                            "type" : "postback",
                            "postback_text" : "Load More...",
                            "payload" : {
                                "url" : "https://www.r.com",
                                "method" : "GET",
                                "payload" : None
                            }
                        },
                        {
                            "label" : "Button 2",
                            "type" : "postback",
                            "postback_text" : "Load More...",
                            "payload" : {
                                "url" : "https://www.r.com",
                                "method" : "GET",
                                "payload" : None
                            }
                        }
                    ]
                },
                {
                    "image" : "https://res.cloudinary.com/hgk8.jpg",
                    "title" : "Gambar 2",
                    "description" : "Carousel single button",
                    "default_action" : {
                        "type" : "postback",
                        "postback_text" : "Load More...",
                        "payload" : {
                            "url" : "https://j.id",
                            "method" : "GET",
                            "payload": None
                        }
                    },
                    "buttons" : [
                        {
                            "label" : "Button 1",
                            "type" : "postback",
                            "postback_text" : "Load More...",
                            "payload" : {
                                "url" : "https://www.r.com",
                                "method" : "GET",
                                "payload" : None
                            }
                        }
                    ]
                }
            ]
        }
        encoded_data = simplejson.dumps(payload).encode("utf-8")
        replay = {
            "access_token" : Controller.access_token,
            "topic_id" : room_id,
            "type" : "carousel",
            "payload" : encoded_data
        }
        carousel = Controller.http.request("POST", Controller.apiurl, fields=replay)
        if carousel.status == 200:
            return jsonify({"status":"success"}), carousel.status
        else:
            return jsonify({"status":"error"}), carousel.status 

    #contoh penggunaan api post-comment untuk jenis card
    def replyCommandCard(room_id):
        payload = {
            "text" : "Special deal buat sista nih..",
            "image" : "https://cdns.img.com/a.jpg",
            "title" : "Gambar 1",
            "description" : "Card Double Button",
            "url" : "http://url.com/baju?id=123%26track_from_chat_room=123",
            "buttons" : [
                {
                    "label" : "Button 1",
                    "type" : "postback",
                    "postback_text" : "Load More...",
                    "payload" : {
                        "url" : "#",
                        "method" : "GET",
                        "payload" : None
                    }
                },
                {
                    "label" : "Button 2",
                    "type" : "postback",
                    "postback_text" : "Load More...",
                    "payload" : {
                        "url" : "#",
                        "method" : "GET",
                        "payload" : None
                    }
                }
            ]
        }
        encoded_data = simplejson.dumps(payload).encode("utf-8")
        replay = {
            "access_token" : Controller.access_token,
            "topic_id" : room_id,
            "type" : "card",
            "payload" : encoded_data
        }
        card  = Controller.http.request("POST", Controller.apiurl, fields=replay)
        if card.status == 200:
            return jsonify({"status":"success"}), card.status
        else:
            return jsonify({"status":"error"}), card.status        

    #fungsi untuk jalankan bot
    def run():
        Controller.getResponse() #ambil response

        #tampung hasil response ke model
        data = Model(
            Controller.apiResponse["chat_room"]["qiscus_room_id"],
            Controller.apiResponse["message"]["text"],
            Controller.apiResponse["message"]["type"],
            Controller.apiResponse["from"]["fullname"]
        ) 

        #cek jika pesan tidak kosong dan mengandung '/'
        if data.message and data.message[0] == "/":
            #ambil nilai text setelah karakter '/'
            command = data.message.split("/")
            #arahkan command ke fungsi yang dituju
            switcher = {
                "location" : [Controller.replyCommandLocation, [data.room_id]],
                "carousel" : [Controller.replyCommandCarousel, [data.room_id]],
                "button" : [Controller.replyCommandButton, [data.room_id, data.sender]],
                "card" : [Controller.replyCommandCard, [data.room_id]]
            }
            return switcher[command[1]][0](*switcher[command[1]][1]) if command[1] in switcher else Controller.replyCommandText(data.sender, data.message_type, data.room_id) 
        else:
            return Controller.replyCommandText(data.sender, data.message_type, data.room_id)         
        
        
                