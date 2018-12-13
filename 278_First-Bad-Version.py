# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        if n == 1:
            return n
        while left < right:
            mid = (left+right)//2
            if not isBadVersion(left) and isBadVersion(left+1):
                return left+1
            if not isBadVersion(right-1) and isBadVersion(right):
                return right
            if not isBadVersion(mid-1) and isBadVersion(mid):
                return mid
            if not isBadVersion(mid):
                left = mid+1
            else:
                right = mid
            
