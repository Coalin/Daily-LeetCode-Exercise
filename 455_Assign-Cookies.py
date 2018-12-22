class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        g = sorted(g)
        s = sorted(s)
        
        i = 0
        j = 0
        
        while i <= len(g)-1 and j <= len(s)-1:
            if s[j] >= g[i]:
                i += 1
                j += 1
                res += 1
            else:
                j += 1
        
        return res
