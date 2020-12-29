from abc import ABC, abstractmethod

class IEntityIndexerLogic(ABC):

    @abstractmethod
    def createIndex(self, data):
        raise NotImplementedError
