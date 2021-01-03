from abc import ABC, abstractmethod

class ITrieStringHelper(ABC):
    
    @abstractmethod
    def startsWithNoMatchIndex(self, string1, string2):
        raise NotImplementedError