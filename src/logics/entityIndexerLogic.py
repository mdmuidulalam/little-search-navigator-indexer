from src.routes.interfaces.iEntityIndexerLogic import IEntityIndexerLogic

class EntityIndexerLogic(IEntityIndexerLogic):

    def __init__(self):
        self.a = 1

    def createIndex(self, data):
        print(data)
