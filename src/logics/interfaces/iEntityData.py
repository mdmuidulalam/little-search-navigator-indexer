from abc import ABC, abstractmethod

class IEntityData(ABC):

    @abstractmethod
    def setData(self, data):
        raise NotImplementedError

    @abstractmethod
    def insertEntityNode(self):
        raise NotImplementedError

    
