import json
import neo4j

from src.logics.interfaces.iEntityData import IEntityData

# TODO a lot of redundant code will be done in data need to be fixed
class EntityData(IEntityData):
    nodeId = None
    data = None

    def __init__(self, neo4jDriver):
        self.neo4jDriver = neo4jDriver

    def setNodeId(self, nodeId):
        self.NodeId = nodeId
    def getNodeId(self):
        return self.nodeId

    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    
    # TODO Bad Practice used to store json object as string
    def insertEntityNode(self):
        with self.neo4jDriver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
            result = session.run("""CREATE (n:EntityData { jsonData: $jsonData }) 
                RETURN id(n) AS nodeId""", jsonData = json.dumps(self.data))
            self.nodeId = result.single()["nodeId"]
            return self.nodeId
    


    