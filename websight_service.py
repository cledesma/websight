import database
from database import Base
from sqlalchemy.orm import sessionmaker
from node_dao import NodeDao
from watcher_dao import WatcherDao
from node_watcher_dao import NodeWatcherDao
import httplib2

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
            # TODO Should be in different thread
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
        #TODO Send email


