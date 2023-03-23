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


# Exercise II:
# Mar 23, 2023
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        max_dest = nums[0]

        for i in range(1, len(nums)):
            if i <= max_dest:
                max_dest = max(max_dest, i+nums[i])
                if max_dest >= len(nums)-1:
                    return True

        return False
