import json
import calDB as database

from dateutil import parser
from twisted.web import server, resource
from twisted.internet import reactor, task


class Server(resource.Resource):
    
    def getChild(self, name, request):
        return self

    def render_GET(self, request):
        #try:
        path = request.path
        
        if path == '/favicon.ico':
            return ''
        elif path == '/events':
            return self.render_events(request)
        else:
            path = path[1:]
            with open(path) as f:
                return f.read()
        #except Exception as e:
        #    return 'Error: %s' % e

    def render_events(self, request):
        args = request.args
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

    return sorted(eventList, dictCompare)

def dictCompare(first, second):
    try:
        f = parser.parse(first['time'])
        s = parser.parse(second['time'])
    except ValueError:
        return 0

    if f > s: return 1
    elif f < s: return -1
    else: return 0


def periodicScrape():
    ## PUT ANY FUNTION CALLS HERE THAT YOU NEED TO RUN PERIODICALLY
    ## example:
    ## import fbEvents (at the top of the file)
    ## inside this function:
    ## fbEvents.update()  
    ## 
    pass


if __name__ == '__main__':
    site = server.Site(Server())
    reactor.listenTCP(8088, site)
    periodicScrape()
    l = task.LoopingCall(periodicScrape)
    l.start(86400)
    reactor.run()
