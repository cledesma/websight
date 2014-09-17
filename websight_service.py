import database
from database import Base
from sqlalchemy.orm import sessionmaker
from node_dao import NodeDao
from watcher_dao import WatcherDao
from node_watcher_dao import NodeWatcherDao
import httplib2
import smtplib
import os

class WebsightService:

    def __init__(self):
        db = database.init()
        Base.metadata.bind = db
        DBSession = sessionmaker(bind=db)
        self.session = DBSession()
        self.node_dao = NodeDao(self.session)
        self.watcher_dao = WatcherDao(self.session)
        self.node_watcher_dao = NodeWatcherDao(self.session)

    def register_node_watcher(self, url, email):
        print "begin register_node_watcher"
        node_id = self.node_dao.create(url)
        watcher_id = self.watcher_dao.create(email)
        self.node_watcher_dao.create(node_id, watcher_id)

    def loop_through_nodes(self):
        print "*** begin loop_through_nodes ***"
        nodes = self.node_dao.get_nodes()        
        for node in nodes:
            # TODO Should be in different threads
            try:
                self.check_site(node)
            except Exception, e:
                self.notify_watchers(node, str(e))
        print "*** end loop_through_nodes ***"

    def check_site(self, node):
        print "begin check_site"
        print "Node: " + node.url
        http = httplib2.Http()
        response = http.request(node.url, "HEAD")
        status = int(response[0]['status'])
        assert status < 400
        print "Status: " + str(status)

    def notify_watchers(self, node, exception):
        print "begin notify_watchers"
        print "Exception: " + exception
        node_watchers = self.node_watcher_dao.get_node_watchers(node.id)
        watchers = self.watcher_dao.get_watchers(node_watchers)
        watchers_list = []
        for watcher in watchers:
            watchers_list.append(watcher.email)
        self.send_mail(watchers_list,exception)

    def send_mail(self,watchers,exception):
        try: 
            print "begin send_mail"
            print "Watchers: " + str(watchers)
            email_username = os.environ['WEBSIGHT_MAIL_USERNAME']
            email_password = os.environ['WEBSIGHT_MAIL_PASSWORD']
            to_list = []
            cc_list = []
            bcc_list = watchers
            header  = 'From: %s\n' % os.environ['WEBSIGHT_MAIL_USERNAME']
            header += 'To: %s\n' % ','.join(to_list)
            header += 'Cc: %s\n' % ','.join(cc_list)
            header += 'Subject: %s\n\n' % "Website is unreachable"
            message = header + exception
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.starttls()
            smtp_server.login(email_username, email_password)
            smtp_server.sendmail(email_username, bcc_list, message)
            smtp_server.quit()
            print "end send_mail"
        except Exception, e:
            print "Exception: " + str(e)



