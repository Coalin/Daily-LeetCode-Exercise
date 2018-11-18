class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res_dic = {}
        res = []
        for i in range(len(s)-9):
            if s[i:i+10] in res_dic:
                res_dic[s[i:i+10]] += 1
            else:
                res_dic[s[i:i+10]] = 1
        for j in res_dic:
            if res_dic[j] >= 2:
                res.append(j)
        return res
        
