from abc import ABC, abstractmethod

class ITrie(ABC):

    @abstractmethod
    def insertWord(self, rootId, word, dataNodeId):
        raise NotImplementedError
