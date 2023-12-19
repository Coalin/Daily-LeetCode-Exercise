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
        
        
# Exercise Ii:
# Dec 18, 2023
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_dict = {}
        s_dict = {}
        s_list = s.split(' ')

        for i in range(len(pattern)):
            if pattern[i] in p_dict:
                p_dict[pattern[i]].append(i)
            else:
                p_dict[pattern[i]] = [i]

        for j in range(len(s_list)):
            if s_list[j] in s_dict:
                s_dict[s_list[j]].append(j)
            else:
                s_dict[s_list[j]] = [j]

        p_res = []
        s_res = []

        for m in p_dict:
            p_res.append(p_dict[m])

        for n in s_dict:
            s_res.append(s_dict[n])

        return p_res == s_res
