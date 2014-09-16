import database
from database import Base
from sqlalchemy.orm import sessionmaker
from node_dao import NodeDao
from watcher_dao import WatcherDao
from node_watcher_dao import NodeWatcherDao

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
        node_id = self.node_dao.create(url)
        watcher_id = self.watcher_dao.create(email)
        self.node_watcher_dao.create(node_id, watcher_id)

