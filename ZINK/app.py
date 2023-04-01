from flask import Flask, request
from model.product import Product

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



