from mock import Mock
import unittest, json
from webserver import Server




class TestServer(unittest.TestCase):

    def test_GET1(self):
        headers = {'subscriptions' : json.dumps(['a', 'b']), 'location' : json.dumps('123')}
        request = Mock()
        request.getHeaders = Mock(return_value=headers)
        request.path = ''

        s = Server()
        
        print "GET1 result:", s.render_GET(request)
        



if __name__ == '__main__':
    unittest.main()
