from database import Watcher

class WatcherDao:

    def __init__(self, session):
        self.session = session

    def create(self, email):
        watcher = self.get_or_create_watcher(self.session, email)
        return watcher.id

    def get_or_create_watcher(self, session, email):
        watcher = session.query(Watcher).filter_by(email=email).first()
        if watcher is None:
            print "Existing Watcher is none"
            watcher = Watcher(email=email)
            session.add(watcher)
            session.commit()
        else:
            print "Existing Watcher: " + watcher.email
        return watcher  

    def get_watchers(self, node_watchers):
        watchers = []
        for node_watcher in node_watchers:
            watcher = self.session.query(Watcher).filter_by(id=node_watcher.watcher_id).first();
            watchers.append(watcher)
            print "Adding watcher: " + watcher.email
        print "Watchers count: " + str(len(watchers))
        return watchers
