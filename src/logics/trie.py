from src.logics.interfaces.iTrie import ITrie

class Trie(ITrie):
    def __init__(self):
        self.a = 1
    # def __init__(self, neo4jData):
    #     self.neo4jData = neo4jData
    
    def insertWord(self, rootId, word, dataNodeId):
        print(rootId, word, dataNodeId)

        # result = self.neo4jData.GetStartsWithMatchNode(rootId, word)
        # matchedStartsWithSting = result.getMatchedStartsWithSting()
        # nodeId = result.getNodeId()

        # if matchedStartsWithSting == word:
        #     self.neo4jData.InsertRelation(nodeId, dataNodeId)
        # else:
        #     #TODO Breaking node or just attach branch. 2 variation needs to be in implemented
        #     newNodeKey = word[len(matchedStartsWithSting): ]
        #     self.neo4jData.InsertBranch(nodeId, dataNodeId, matchedStartsWithSting, newNodeKey)