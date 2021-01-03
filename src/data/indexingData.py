import neo4j

from src.logics.interfaces.iIndexingData import IIndexingData

class IndexingData(IIndexingData):
    nodeId = None
    
    def __init__(self, neo4jDriver):
        self.neo4jDriver = neo4jDriver

    def setNodeId(self, nodeId):
        self.nodeId = nodeId

    def getNode(self, label):
        with self.neo4jDriver.session() as session:
            result = session.run("MATCH (n:" +label+ ") RETURN n as node")
            record = result.single()
            return self.node
    
    def getNextNode(self, relationKey):
        with self.neo4jDriver.session() as session:
            result = session.run("""MATCH (n) - [r:TrieRelation] -> (next)
                WHERE r.key = $key and id(n) = $nodeId
                RETURN Id(next) as nextNodeId, next.subString as nextNodeSubString""", nodeId = self.nodeId, key= relationKey)
            record = result.single()

            if record == None:
                return None, None
            else:
                return record["nextNodeId"], record["nextNodeSubString"]
    
    def insertIndexerNode(self, parentNodeId, subString):
        with self.neo4jDriver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
            result = session.run("""MATCH (parent)
                WHERE Id(parent) = $parentNodeId
                CREATE (n:TrieNode { subString: $subString })
                CREATE (parent) - [r:TrieRelation {key: $key}] -> (n)
                RETURN id(n) AS nodeId""", subString = subString, key= subString[0], parentNodeId = parentNodeId)
            self.nodeId = result.single()["nodeId"]
            return self.nodeId