# Exercise I:
# May 21, 2023

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 0 
        res = ''

        while i < len(str1):
            if str1[:i+1]*(len(str1)//(i+1)) == str1 and str1[:i+1]*(len(str2)//(i+1)) == str2:
                res = str1[:i+1]
            i += 1

        return res
