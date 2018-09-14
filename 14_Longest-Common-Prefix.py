class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        res = strs[0]
        for item in strs[1:]:
            break_point = min(len(res), len(item))
            for i in range(break_point):
                if res[i] != item[i]:
                    break_point = i
                    break
            res = res[:break_point]
        return res
    
# 54.72%; 56ms.
