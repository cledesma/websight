import database
from database import Watcher, Node, Base
from sqlalchemy.orm import sessionmaker
from node_dao import NodeDao
from watcher_dao import WatcherDao

class WebsightService:

	def __init__(self):
		db = database.init()
		Base.metadata.bind = db
		DBSession = sessionmaker(bind=db)
		self.session = DBSession()
		self.node_dao = NodeDao(self.session)
		self.watcher_dao = WatcherDao(self.session)

	def create_node(self, url):
		self.node_dao.create(url)

	def create_watcher(self, email):
		self.watcher_dao.create(email)


