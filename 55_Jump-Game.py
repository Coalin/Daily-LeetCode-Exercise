class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        reach = nums[0]
        while i <= len(nums)-1 and i <= reach:
            reach = max(reach, i+nums[i])
            i += 1
        return reach >= len(nums)-1

# 62.44%; 72ms.
