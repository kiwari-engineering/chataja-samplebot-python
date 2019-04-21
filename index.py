# @authors: Iskandar Suhaimi
# @email: hello@iskandarsuhaimi.com

from flask import Flask
from app.controller import Controller

app = Flask(__name__)

@app.route("/", methods=['POST'])
def run():
    return Controller.run()
