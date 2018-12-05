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
    
        
