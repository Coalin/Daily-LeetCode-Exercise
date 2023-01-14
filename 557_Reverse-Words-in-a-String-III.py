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
        

# Exercise II:
# Jan 14, 2023
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        
        s_list = s.split(' ')
        for s_word in s_list:
            res.append(s_word[::-1])

        return ' '.join(res)
