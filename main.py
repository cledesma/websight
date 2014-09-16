from flask import Flask
import database

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

if __name__== "__main__":
	database.init()
	app.run()

