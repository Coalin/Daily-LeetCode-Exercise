class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
# Method I:
#        if len(s) == 0:
#            return ''
#        else:
#            return self.reverseString(s[1:]) + s[0]
        
# Method II:
#        res = ''
#        for i in reversed(s):
#            res += i
#        return res

# Method III:
        return s[::-1]


# Exercise IV
# Jan 14, 2023
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            tmp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = tmp 

        return s
