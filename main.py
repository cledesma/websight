from flask import Flask
from websight_service import WebsightService

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__== "__main__":
    app.run()

