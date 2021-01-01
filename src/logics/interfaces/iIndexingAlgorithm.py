from abc import ABC, abstractmethod

class IIndexingAlgorithm(ABC):

    @abstractmethod
    def createIndex(self, data, rootId, dataNodeId):
        raise NotImplementedError
