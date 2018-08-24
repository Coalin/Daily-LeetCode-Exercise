class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1 and n cannot exist at the same time 
        # dp[n] = max(dp[1~n-1], dp[2~n])
        
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        if len(nums)==3:
            return max(nums[0], nums[1], nums[2])
        else:
            dp = [0 for col in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            dp[2] = max(nums[0]+nums[2], nums[1])
            for i in range(3, len(nums)):
                dp[i] = max(self.rob_(nums[:i]), self.rob_(nums[1:i+1]))
        return dp[-1]
    
    def rob_(self, nums):
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
        
        
