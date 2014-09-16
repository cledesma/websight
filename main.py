from flask import Flask
from websight_service import WebsightService

from database import Node

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__== "__main__":
    srv = WebsightService()
    srv.register_node_watcher('http://dev.ewise.com', 'cledesma@ewise.com')

    node = Node(id=1)
    srv.notify_watchers(node)

    app.run()

