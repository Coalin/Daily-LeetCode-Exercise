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
        
        
