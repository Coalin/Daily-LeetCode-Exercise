class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0/self.myPow(x, -n)
        tmp = self.myPow(x, n/2)
        if n%2 == 0:
            return tmp*tmp
        if n%2 == 1:
            return x*tmp*tmp
        
        
# Exercise II:
# Jan 31, 2024
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1 
        if n < 0:
            return 1/self.myPow(x, -n)
        half = self.myPow(x, n//2)
        if n%2 == 0:
            return half*half
        else:
            return x*half*half
