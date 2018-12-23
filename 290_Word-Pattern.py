class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_ = str.split(" ")
        dic_s = {}
        dic_p = {}
        res_s = []
        res_p = []
        
        for i in range(len(str_)):
            if str_[i] in dic_s:
                dic_s[str_[i]].append(i)
            else:
                dic_s[str_[i]] = [i]
                
        for j in range(len(pattern)):
            if pattern[j] in dic_p:
                dic_p[pattern[j]].append(j)
            else:
                dic_p[pattern[j]] = [j]
        
        for x in dic_s:
            res_s.append(dic_s[x])
        
        for y in dic_p:
            res_p.append(dic_p[y])
            
        return res_s == res_p
        
        
