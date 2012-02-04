from mock import Mock
import unittest, json
from webserver import Server
import webserver



class TestServer(unittest.TestCase):

    # def test_GET(self):
    #     headers = {'subscriptions' : json.dumps(['a', 'b']), 'location' : json.dumps('123')}
    #     request = Mock()
    #     request.getHeaders = Mock(return_value=headers)
    #     request.path = ''

    #     s = Server()
        
    #     print "GET result:", s.render_GET(request)


    def test_EventData(self):
        subscriptions = [dict(time='March 3rd'), dict(time='Feb 5th'), dict(time='jan 2nd')]
        location = 'loc'

        print 'XXXXX', webserver.getEventData(subscriptions, location)


if __name__ == '__main__':
    unittest.main()
