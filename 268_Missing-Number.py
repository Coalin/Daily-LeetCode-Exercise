# Exercise I:
# Apr 8, 2023

class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        res = 0 

        for i in range(len(nums)):
            res ^= nums[i]
            res ^= (i+1) 

        return res
