from database import NodeWatcher

class NodeWatcherDao:

    def __init__(self, session):
        self.session = session

    def create(self, node_id, watcher_id):
        # new_node_watcher = NodeWatcher(node_id=node_id, watcher_id=watcher_id)
        # self.session.add(new_node_watcher)
        # self.session.commit()
        self.get_or_create_node_watcher(self.session, node_id, watcher_id)

    def get_or_create_node_watcher(self, session, node_id, watcher_id):
        node_watcher = session.query(NodeWatcher).filter_by(node_id=node_id,watcher_id=watcher_id).first()
        if node_watcher is None:
            print "Existing Node Watcher is none"
            node_watcher = NodeWatcher(node_id=node_id,watcher_id=watcher_id)
            session.add(node_watcher)
            session.commit()
        else:
            print "Existing Node ID: " + str(node_watcher.node_id) + " Existing Watcher ID: " + str(node_watcher.watcher_id)
        return node_watcher