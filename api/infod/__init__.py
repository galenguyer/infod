from flask import Flask
from config import Config
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Config)
app.config["JSON_SORT_KEYS"] = False

_client = MongoClient(app.config["SQUIRREL_MONGO_URI"])
_db = _client["dump1090"]
db = _db["aircraft"]

from infod import routes, errors


@app.after_request
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response
