from abc import ABC, abstractmethod

class IIndexingData(ABC):

    @abstractmethod
    def getNodeId(self, label):
        raise NotImplementedError
