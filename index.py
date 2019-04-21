# @authors: Iskandar Suhaimi
# @email: hello@iskandarsuhaimi.com

from flask import Flask
from app.controller import Controller #panggil controller

app = Flask(__name__) #inisiasi aplikasi flask

@app.route("/", methods=['POST']) #jalankan bot pada url root ('/')
def run():
    return Controller.run() #panggil method run controller
