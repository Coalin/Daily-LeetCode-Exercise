class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        str_dic = {}
        for i in range(len(s)):
            if s[i] in str_dic:
                str_dic[s[i]] += 1
            else:
                str_dic[s[i]] = 1
        for j in range(len(t)):
            if t[j] in str_dic:
                str_dic[t[j]] -= 1
                if str_dic[t[j]] == -1:
                    return t[j]
            else:
                return t[j]
        return None
        
