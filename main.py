from flask import Flask
from websight_service import WebsightService
from apscheduler.schedulers.background import BackgroundScheduler
import logging 

logging.basicConfig()
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__== "__main__":
    print "starting websight"
    srv = WebsightService()
    scheduler = BackgroundScheduler()

    @scheduler.scheduled_job('interval', minutes=1)
    def loop_job():
        srv.loop_through_nodes()

    print "begin scheduler"
    scheduler.start()
    print "begin app server"
    app.run()

