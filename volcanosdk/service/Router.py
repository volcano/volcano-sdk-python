import json

class Router:
    def __init__(self):
        self.routes = None
    
    def find(self, service):
        
        if not self.routes:
            self.loadServiceData()
            
        if not service in self.routes:
            return False
        
        return self.routes[service]
        
    
    def loadServiceData(self):
        file = open('../config/routes.json', 'r')
        
        contents = file.read()
        self.routes = json.loads(contents)
        
        pass