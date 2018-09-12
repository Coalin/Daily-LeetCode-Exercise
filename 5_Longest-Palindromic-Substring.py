class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = right = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-2 > right-left:
                left = l+1
                right = r-1
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-2 > right-left:
                left = l+1
                right = r-1
        return s[left:right+1]
        
# 65.95%; 820 ms
