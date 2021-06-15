from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config["JSON_SORT_KEYS"] = False

from infod import routes, errors


@app.after_request
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response
