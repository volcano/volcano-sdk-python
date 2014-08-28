import service.Router as Router

class Service:
    def __init__(self, service):
        self._service = service
        
        self.getRoutes()
        pass
    
    def getRoutes(self):
        self._routes = Router.find(self._service)
        
        if not self._routes:
            raise Exception("No routes for service {0}".format(self._service))
    
    def call(self, method, *args):
        """
        Does the actual api call.
        """
        pass
    
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