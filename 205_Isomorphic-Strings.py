class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s = {}
        dic_t = {}
        res_s = []
        res_t = []

        for i in range(len(s)):
            if s[i] in dic_s:
                dic_s[s[i]].append(i)
            else:
                dic_s[s[i]] = [i]
                
        for j in range(len(t)):
            if t[j] in dic_t:
                dic_t[t[j]].append(j)
            else:
                dic_t[t[j]] = [j]
        
        for x in dic_s:
            res_s.append(dic_s[x])
            
        for y in dic_t:
            res_t.append(dic_t[y])
            
        return res_s == res_t
        
        
        
