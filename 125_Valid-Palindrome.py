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
