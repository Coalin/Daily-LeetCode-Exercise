class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum([int(x) for x in list(str(bin(x^y)))[2:]])
        
        
