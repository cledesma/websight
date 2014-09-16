from flask import Flask
import database
from websight_service import WebsightService

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

if __name__== "__main__":
	db = database.init()
	srv = WebsightService(db)
	srv.add_node('http://www.google.com')
	app.run()

