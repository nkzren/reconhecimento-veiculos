import redis
from flask import Flask

app = Flask(__name__)

redis = redis.Redis(host="localhost",port=6389, db=0)

@app.route("/")
def hello_world():
    print("HEllo World")
    return "Hello World"


