# Exercise I:    
# 54.72%; 56ms.
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


# Exercise II:
# Feb 23, 2019
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        pre = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j <= min(len(pre), len(strs[i]))-1:
                if pre[j] == strs[i][j]: 
                    j += 1
                else:
                    break
            pre = pre[:j][:]
            
        return pre
            
            
        
        
