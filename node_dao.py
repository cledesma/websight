from database import Node

class NodeDao:

	def __init__(self, session):
		self.session = session

	def create(self, url):
		new_node = Node(url=url)
		self.session.add(new_node)
		self.session.commit()
