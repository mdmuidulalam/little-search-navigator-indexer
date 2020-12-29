class suffixTreeIndexing:

    def __init__(self, trieLogic, stringHelper, allowedChar):
        self.trieLogic = trieLogic
        self.stringHelper = stringHelper
        self.allowedChar = allowedChar

    def createIndex(self, data, separators):
        indexAttributes = data.getIndexAttributes()

        for attr in indexAttributes:
            words = stringHelper.stringSeparate(str(data[attr]), separators)
            for word in words:
                word = stringHelper.removeChar(word, allowedChar)
                self.trieLogic.insertWord(rootId, word, dataNodeId)