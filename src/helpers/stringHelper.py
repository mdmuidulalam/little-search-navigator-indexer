from src.logics.interfaces.iTrieStringHelper import ITrieStringHelper

class StringHelper(ITrieStringHelper):

    def startsWithNoMatchIndex(self, string1, string2):
        if len(string1) == len(string2):
            return -1

        i = 0
        while i < len(string1) and i < len(string2) and string1[i] == string2[i]:
            i += 1
        return i