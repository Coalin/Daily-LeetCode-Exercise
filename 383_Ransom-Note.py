class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom = dict()
        mag = dict()
        
        for i in ransomNote:
            if i in ransom:
                ransom[i] += 1
            else:
                ransom[i] = 1
                
        for j in magazine:
            if j in mag:
                mag[j] += 1
            else:
                mag[j] = 1
        
        for x in ransom:
            if x not in mag:
                return False
            else:
                if ransom[x] > mag[x]:
                    return False
        
        return True
        
