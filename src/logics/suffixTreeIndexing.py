from src.helpers.staticHelper import StaticHelper
from src.logics.interfaces.iIndexingAlgorithm import IIndexingAlgorithm
from src.logics.interfaces.iTrie import ITrie

from src.logics.interfaces.iIndexingData import IIndexingData

class SuffixTreeIndexing(IIndexingAlgorithm):
    def __init__(self, trie, indexingData):
        self.trie = trie
        StaticHelper.isInterfaceResloved(self.trie, ITrie)
        self.indexingData = indexingData
        StaticHelper.isInterfaceResloved(self.indexingData, IIndexingData)
        #self.stringHelper = stringHelper

    def createIndex(self, data, rootId, dataNodeId, allowedChar, separators):
        self.trie.insertWord(rootId, "bad", dataNodeId)

        # indexAttributes = data.getIndexAttributes()

        # for attr in indexAttributes:
        #     words = stringHelper.stringSeparate(str(data[attr]), separators)
        #     for word in words:
        #         word = stringHelper.removeChar(word, allowedChar)
        #         self.trie.insertWord(rootId, word, dataNodeId)