from database import Watcher

class WatcherDao:

	def __init__(self, session):
		self.session = session

	def create(self, email):
		new_watcher = Watcher(email=email)
		self.session.add(new_watcher)
		self.session.commit()

