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
            
            
# Exercise III:
# Dec 24, 2022
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for i in range(1, len(strs)):
            res = self.lcp(res, strs[i])

        return res

    def lcp(self, str1, str2):
        len_min = min(len(str1), len(str2))
        idx = 0 
        while idx < len_min:
            if str1[idx] != str2[idx]:
                break 
            idx += 1
        return str1[:idx]
        
        
