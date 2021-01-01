from src.logics.interfaces.iIndexingData import IIndexingData

class IndexingData(IIndexingData):
    nodeId = None

    def __init__(self, neo4jDriver):
        self.neo4jDriver = neo4jDriver

    def getNodeId(self, label):
        with self.neo4jDriver.session() as session:
            result = session.run("MATCH (n:" +label+ ") RETURN Id(n) AS nodeId")
            self.nodeId = result.single()["nodeId"]
            return self.nodeId