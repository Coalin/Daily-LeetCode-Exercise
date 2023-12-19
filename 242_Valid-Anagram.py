# Exercise I:
# Dec 19, 2023

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1

        for j in range(len(t)):
            if t[j] not in s_dict:
                return False
            elif s_dict[t[j]] <= 0:
                return False 
            else:
                s_dict[t[j]] -= 1

        return True
