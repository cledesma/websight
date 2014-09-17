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

    def get_nodes(self):
        nodes = self.session.query(Node).all()
        print "Nodes count: " + str(len(nodes))
        return nodes

    def get_node(self, id):
        node = self.session.query(Node).filter_by(id=id).first()
        print "Node ID: " + str(node.id)
        print "Node URL: " + node.url