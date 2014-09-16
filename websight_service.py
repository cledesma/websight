from database import Watcher, Node, Base
from sqlalchemy.orm import sessionmaker

class WebsightService:

	def __init__(self, db):
		self.db = db
		Base.metadata.bind = db
		DBSession = sessionmaker(bind=db)
		self.session = DBSession()

	def add_node(self, url):
		new_node = Node(url=url)
		self.session.add(new_node)
		self.session.commit()
