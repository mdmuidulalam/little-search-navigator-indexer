from abc import ABC, abstractmethod

class IIndexingData(ABC):

    @abstractmethod
    def setNodeId(self, nodeId):
        raise NotImplementedError

    @abstractmethod
    def getNode(self, label):
        raise NotImplementedError

    @abstractmethod
    def getNextNode(self, relationKey):
        raise NotImplementedError

    @abstractmethod
    def insertIndexerNode(self, parentNodeId, subString):
        raise NotImplementedError
