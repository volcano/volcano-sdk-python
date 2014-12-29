import json, os

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
        curpath = os.path.dirname(os.path.realpath(__file__))
        file = open(curpath + '/../config/routes.json', 'r')
        
        contents = file.read()
        self.routes = json.loads(contents)
        
        pass