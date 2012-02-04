import json
import calDB as database

from twisted.web import server, resource
from twisted.internet import reactor


class Server(resource.Resource):
    
    def getChild(self, name, request):
        return self

    def render_GET(self, request):
        args = request.args
        path = request.path

        if path == '/favicon.ico':
            return ''

        try:
            subscriptions = args['subscriptions'][0].split(',')
            subscriptions = [str(s) for s in subscriptions]
        except (KeyError, TypeError, IndexError) as e:
            subscriptions = []
            print 'Subscriptions header missing from headers: %s' % e
        
        try:
            location = args['location'][0]
        except (KeyError, TypeError, IndexError) as e:
            location = ''
            print 'Locations header missing from headers: %s' % e

        data = getEventData(subscriptions, location)
        return json.dumps(data)
        
    def render_POST(self, request):
        return self.render_GET(request)

def getEventData(subscriptions, location):
    eventList = []
    for sub in subscriptions:
        events = database.getEvents(sub)
        eventList += events

    #sorted(eventList, dictCompare)
    return eventList

def dictCompare(first, second):
    f = first['time']
    s = second['time']
    if f > s: return 1
    elif f < 2: return -1
    else: return 0



if __name__ == '__main__':
    site = server.Site(Server())
    reactor.listenTCP(8088, site)
    reactor.run()
