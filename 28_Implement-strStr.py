class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
        elif len(haystack) < len(needle):
            return -1
        else:
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1


# Exercise II:
# Apr 5, 2023
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i 

        return -1
