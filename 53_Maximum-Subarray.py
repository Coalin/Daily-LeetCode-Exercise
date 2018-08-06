class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = -10000000000
        cursum = -10000000000
        for num in nums:
            cursum = max(num, cursum+num)
            maxsum = max(cursum, maxsum)
        return maxsum
