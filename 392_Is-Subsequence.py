# Exercise I:
# Apr 15, 2023

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        i = 0 
        j = 0 

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
    
        if i == len(s):
            return True 

        return False


# Exercise II:
# Dec 13, 2023
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        left = 0 
        right = 0 

        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
            right += 1 

        if left == len(s):
            return True

        return False
