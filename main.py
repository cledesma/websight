from flask import Flask
from websight_service import WebsightService

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

if __name__== "__main__":
	srv = WebsightService()
	srv.create_node('http://www.ewise.com')
	srv.create_watcher('carlo@devcon.ph')
	app.run()

