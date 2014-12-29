from volcanosdk.service.Router import Router
import urllib2, json

class Service:
    def __init__(self, service):
        """
        Constructor, figures out routes.
        """
        self._service = service
        self._returnRaw = False
        self.getRoutes()
    
    def getRoutes(self):
        router = Router()
        self._routes = router.find(self._service)
        
        if not self._routes:
            raise Exception("No routes for service {0}".format(self._service))
    
    def __getattr__(self, attr):
        """
        Pass undefined calls along to the call method
        """
        def method(*args, **kwargs):
            return self.call(attr, *args)
        
        return method
    
    def call(self, route, *args):
        """
        Does the actual api call.
        """
        
        if not self._routes[route]:
            raise Exception("No route defined for {}".format(route))
        
        data = None
        
        if isinstance(args[len(args)-1], list):
            data = args[len(args)-1]
        
        # Offset starts at 1.
        url = self._baseUrl + "/" + self._routes[route]['path'].format(None, *args)
        
        req = urllib2.Request(url, data)
        req.get_method = lambda: self._routes[route]['method']
        
        resp = urllib2.urlopen(req)
        
        if not self._returnRaw:
            return json.loads(resp.read())
        
        return resp.read()
    
    def apiKey(self, key = None):
        """
        Getter/Setter for api keys
        """
        if (key) :
            self._apikey = key
            return self
            
        return self._apikey
        
    def baseUrl(self, url = None):
        """
        Getter/Setter for base url
        """
        if (url):
            self._baseUrl = url
            return self
            
        return self._baseUrl
        
    def returnRaw(self, raw = None):
        """
        Getter/Setter for base url
        """
        if (raw):
            self._returnRaw = raw
            return self
            
        return self._returnRaw