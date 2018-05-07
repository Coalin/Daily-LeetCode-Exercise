class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start = 0
        ans = 0
        for i in xrange(len(s)):
            if s[i] in d:
                start = max(start, d[s[i]]+1)
            d[s[i]] = i
            ans = max(ans, i-start+1)
        return ans
