from src.helpers.staticHelper import StaticHelper
from src.logics.interfaces.iTrieStringHelper import ITrieStringHelper
from src.logics.interfaces.iTrie import ITrie
from src.logics.interfaces.iIndexingData import IIndexingData

class Trie(ITrie):
    def __init__(self, indexingData, stringHelper):
        self.indexingData = indexingData
        StaticHelper.isInterfaceResloved(self.indexingData, IIndexingData)
        self.stringHelper = stringHelper
        StaticHelper.isInterfaceResloved(self.stringHelper, ITrieStringHelper)
    
    def insertWord(self, rootId, word, dataNodeId):
        currentNodeId = rootId
        word = 'bacadama'
        while word != '':
            self.indexingData.setNodeId(currentNodeId)
            childNodeId, childNodeSubString = self.indexingData.getNextNode(word[0])
            print(childNodeId, childNodeSubString)

            if childNodeId != None :
                if word == childNodeSubString:
                    # TODO Connect data node here
                    word = ''
                elif word.startswith(childNodeSubString):
                    word = word[len(childNodeSubString):]
                    currentNodeId = childNodeId
                else:
                    noMatchIndex = self.startsWithNoMatchIndex(word, childNodeSubString)
                    commonStartWith = childNode.subString[:noMatchIndex]
                    notMatchedSubsting = childNode.subString[noMatchIndex:]
                    notMatchedWord = word[noMatchIndex:]
                    
                    newNode = TrieNode(commonStartWith)
                    newNode.childNodes[childNodeSubString[noMatchIndex]] = newNode
                    childNode.subString = notMatchedSubsting
                    current.childNodes[word[0]] = newNode

                    if len(word) != noMatchIndex:
                        newNode2 = TrieNode(word[noMatchIndex:])
                        newNode.childNodes[word[noMatchIndex]] = newNode2
                    word = ''
            else:
                self.indexingData.insertIndexerNode(currentNodeId, word)
                # TODO Then Connect DataNode
                word = ''