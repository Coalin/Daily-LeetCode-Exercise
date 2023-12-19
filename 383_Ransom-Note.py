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
        

# Exercise II:
# Dec 17, 2023
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        resource_dict = dict()

        for k in magazine:
            if k in resource_dict:
                resource_dict[k] += 1
            else:
                resource_dict[k] = 1

        for s in ransomNote:
            if s not in resource_dict:
                return False
            elif resource_dict[s] <= 0:
                return False 
            else:
                resource_dict[s] -= 1

        return True
