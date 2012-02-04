from twisted.web import server, resource
from twisted.internet import reactor

class Server(resource.Resource):
    
    def getChild(self, name, request):
        return self

    def render_GET(self, request):
        pass





site = server.Site(Server())
reactor.listenTCP(80, site)
reactor.run()
