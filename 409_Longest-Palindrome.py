class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        hash_table = {}
        
        for word in s:
            if word in hash_table:
                hash_table[word] += 1
            else:
                hash_table[word] = 1
                
        for i in hash_table:
            res += (hash_table[i]//2)*2
        
        for j in hash_table:
            if hash_table[j]%2 == 1:
                res += 1
                break
        
        return res
            
            
