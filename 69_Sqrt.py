class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 0
        right = x
        middle = x//2
        while left+1 < right:
            if middle*middle > x:
                right = middle
            elif middle*middle < x:
                left = middle
            else:
                return middle
                break
            middle = (left+right)//2
        return left


# Exercise II:
# Jan 31, 2024
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0 
        right = x 
        
        while left <= right:
            mid = left + (right-left)//2
            if mid**2 == x:
                return mid 
            if mid**2 > x:
                right = mid-1
            else:
                left = mid+1

        return left-1
