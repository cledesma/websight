import unittest
from database import Node
from websight_service import WebsightService
from node_dao import NodeDao

class TestWebsightService(unittest.TestCase):

    def setUp(self):
        srv = WebsightService()
        srv.register_node_watcher('http://gist.github.com', 'test@gmail.com')
        srv.register_node_watcher('http://www.facebook.com', 'test@gmail.com')
        srv.register_node_watcher('http://dummy.github.com', 'test@gmail.com')

    # TODO Implement properly
    def test_check_site(self):
        srv = WebsightService()
        srv.loop_through_nodes()

if __name__ == '__main__':
    unittest.main()
