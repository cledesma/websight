from database import Node

class NodeDao:

    def __init__(self, session):
        self.session = session

    def create(self, url):
        node = self.get_or_create_node(self.session, url)
        return node.id

    def get_or_create_node(self, session, url):
        node = session.query(Node).filter_by(url=url).first()
        if node is None:
            print "Existing Node is none"
            node = Node(url=url)
            session.add(node)
            session.commit()
        else:
            print "Existing Node: " + node.url
        return node 