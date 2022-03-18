import requests
import json
import re
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    res = requests.get("https://e31.net")

    print(res.text)
    return re.sub('SRC="', 'SRC="http://e31.net/', res.text)
    #return "<p>Hello, World!</p>"

@app.route("/amoge")
def amoge():
    return "<p>sus baka 😳!</p>"