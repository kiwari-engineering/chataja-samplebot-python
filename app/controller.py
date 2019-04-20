import unirest
from model import *
from flask import request, jsonify
from array import *

class Controller:

    def __init__(self):
        self.access_token = ""
        self.apiurl = ""
        self.headers = array()