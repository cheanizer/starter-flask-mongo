import flask
from flask import jsonify
import user_tweets
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET"])
def home():
    twits = user_tweets.proc()
    return twits

app.run()