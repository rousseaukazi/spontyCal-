import json
from twisted.web import server, resource
from twisted.internet import reactor


class Server(resource.Resource):
    
    def getChild(self, name, request):
        return self

    def render_GET(self, request):
        headers = request.getHeaders()
        path = request.path

        print '---- Received Request with path: %s ----' % path
        print 'headers:', headers
        
        try:
            subscriptions = json.loads(headers['subscriptions'])
            subscriptions = [str(s) for s in subscriptions]
        except (KeyError, TypeError) as e:
            subscriptions = []
            print 'Subscriptions header missing from headers: %s' % e
        
        try:
            location = str(json.loads(headers['location']))
        except (KeyError, TypeError) as e:
            location = ''
            print 'Locations header missing from headers: %s' % e

        print 'Subscriptions:', subscriptions
        print 'location', location

        data = getEventData(subscriptions, location)
        print 'DATA result: %s\n\n' % data
        #return json.dumps(data)
        return "ROUSSEAU LICKS BALLS"
        
    def render_POST(self, request):
        return self.render_GET(request)

def dictCompare(first, second):
    f = first['time']
    s = second['time']
    
    if f > s:
        return 1
    elif f < 2:
        return -1
    else:
        return 0

    


def getEventData(subscriptions, location):
    eventList = []
    for sub in subscriptions:
        #events = database.getEvents(sub)
        #eventList += events
        pass

    #sorted(eventList, dictCompare)
    return eventList

if __name__ == '__main__':
    site = server.Site(Server())
    reactor.listenTCP(8088, site)
    reactor.callLater(5, reactor.stop)
    reactor.run()
