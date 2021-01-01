from src.helpers.staticHelper import StaticHelper
from src.logics.interfaces.iIndexingAlgorithm import IIndexingAlgorithm
from src.logics.interfaces.iTrie import ITrie

class SuffixTreeIndexing(IIndexingAlgorithm):
    def __init__(self, trie):
        self.trie = trie
        StaticHelper.isInterfaceResloved(self.trie, ITrie)
        #self.stringHelper = stringHelper

    def createIndex(self, data, rootId, dataNodeId, allowedChar, separators):
        self.trie.insertWord(1, 'Hee', 100)
        # indexAttributes = data.getIndexAttributes()

        # for attr in indexAttributes:
        #     words = stringHelper.stringSeparate(str(data[attr]), separators)
        #     for word in words:
        #         word = stringHelper.removeChar(word, allowedChar)
        #         self.trie.insertWord(rootId, word, dataNodeId)