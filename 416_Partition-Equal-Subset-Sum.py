class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        half_sum = total_sum//2
        dp = [[0 for col in range(half_sum+1)] for row in range(len(nums))]
        for j in range(nums[0], half_sum+1):
            dp[0][j] = nums[0]
        for i in range(1, len(nums)):
            for j in range(nums[i], half_sum+1):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]]+nums[i])
        if dp[len(nums)-1][half_sum] == half_sum:
            return True
        else:
            return False
