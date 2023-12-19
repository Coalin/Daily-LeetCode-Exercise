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
        

# Exercise II:
# Dec 18, 2023
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = [i]
            else:
                s_dict[s[i]].append(i)

        for j in range(len(t)):
            if t[j] not in t_dict:
                t_dict[t[j]] = [j]
            else:
                t_dict[t[j]].append(j)

        res_s = []
        res_t = []

        for m in s_dict:
            res_s.append(s_dict[m])
        
        for n in t_dict:
            res_t.append(t_dict[n])

        return res_s == res_t      
