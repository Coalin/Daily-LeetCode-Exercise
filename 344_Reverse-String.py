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
