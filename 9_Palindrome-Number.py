class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_str = str(x)
        res = ' '
        for i in reversed(range(len(x_str))):
            res += x_str[i]
        return int(res) == x
        
        
