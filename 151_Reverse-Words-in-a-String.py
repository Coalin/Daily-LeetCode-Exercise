class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split(' ')
        word_list = [x for x in word_list if x != '']
        res = ''
        while word_list:
            res += ' ' + word_list.pop().strip()
        return res.strip()
    
    
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_nb = s.strip()
        stack = []
        cur_word = ''

        i = 0
        while i < len(s_nb):
            if s_nb[i] != ' ':
                cur_word += s_nb[i]
            else:
                if cur_word != '':
                    stack.append(cur_word)
                cur_word = ''
            i += 1
        
        res = cur_word+' '
        while stack:
            res += stack.pop()
            res += ' '
        
        return res.strip() 


# Exercise III:
# June 2, 2023 
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        
        res = ''
        for word in reversed(s_list):
            if word != '':
                res += word
                res += ' ' 

        return res.strip()
