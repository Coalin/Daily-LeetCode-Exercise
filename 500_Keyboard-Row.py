class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for word in words:
            if self.isWordPrintable(word):
                res.append(word)
                
        return res
        
    def isWordPrintable(self, word):
        if len(word) == 1:
            return True
        
        for i in range(1, len(word)):
            if self.letterClassification(word[i]) != self.letterClassification(word[i-1]):
                return False
        return True
        
    
    def letterClassification(self, letter):
        if letter.lower() in ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']:
            return 1
        elif letter.lower() in ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']:
            return 2
        else:
            return 3
