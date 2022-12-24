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
        
        
# Exercise II:
class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        return str(x) == str(x)[::-1]
        
        
# Exercise III:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        origin = x
        revert_number = 0 
        while x > 0:
            revert_number = revert_number*10+x%10
            x = x//10

        return revert_number == origin
