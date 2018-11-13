class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(" ")
        res = ""
        for item in s_list:
            res += (" "+item[::-1])
        return res.strip()
        
