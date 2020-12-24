class Solution:
    def firstUniqChar(self, s: str) -> int:
        alpha = {}
        for char in s:
            if char in alpha:
                alpha[char] += 1
            else:
                alpha[char] = 1
        
        for i in range(len(s)):
            if alpha[s[i]] == 1:
                return i
        
        return -1
        