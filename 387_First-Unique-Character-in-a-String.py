class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        res_dic = {}
        for i in s:
            if i in res_dic:
                res_dic[i] += 1
            else:
                res_dic[i] = 1
        for j in range(len(s)):
            if res_dic[s[j]] == 1:
                return j
        return -1
        
