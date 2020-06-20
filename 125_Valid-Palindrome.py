class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = re.sub("[^A-Za-z0-9]", "", s).lower()
        s_ = ''
        for i in reversed(s):
            s_ += i
        if s_ == s:
            return True
        else:
            return False


import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res_list = []

        for word in s:
            if re.match( r'[a-zA-Z0-9]', word, re.I):
                res_list.append(word.lower())

        return res_list == res_list[::-1]