class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        else:
            dp = [0 for col in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
            
        
# Exercise II
# Mar 18, 2023
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        # 不选
        dp[0][0] = 0
        # 选
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = max(dp[i-1][0]+nums[i], dp[i-1][1])

        return max(dp[-1][0], dp[-1][1])


# Exercise III
# Sep 28, 2023
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        max_amt = [0 for _ in range(len(nums))]
        max_amt[0] = nums[0]
        max_amt[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            max_amt[i] = max(max_amt[i-2]+nums[i], max_amt[i-1])

        return max_amt[-1]
