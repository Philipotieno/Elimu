#views of the server
from run import app
from flask import Flask

@app.route('/')
def index():
    return jsonify({"Message": "Hello Welcome to my homepage"})