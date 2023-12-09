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


# Exercise II:
# Dec 9, 2023
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1 
        cur_set = set()
        left = 0
        right = 0

        if not s:
            return 0

        while right < len(s):
            if s[right] not in cur_set:
                cur_set.add(s[right])
                res = max(res, len(cur_set))
                right += 1
            else:
                cur_set.remove(s[left])
                left += 1

        return res