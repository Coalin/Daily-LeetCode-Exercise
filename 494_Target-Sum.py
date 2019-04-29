# Method I:
# DFS 超时
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.res = 0
        self.dfs(nums, 0, S)
        return self.res
    
    def dfs(self,nums, index, S):
        if index == len(nums):
            if S == 0:
                self.res += 1
        else:
            self.dfs(nums, index+1, S+nums[index])
            self.dfs(nums, index+1, S-nums[index])
   

# Method II:
# DP
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [dict() for _ in range(len(nums))]
        
        if nums[0]:
            dp[0][nums[0]] = 1
            dp[0][-nums[0]] = 1
        else:
            dp[0][nums[0]] = 2
            dp[0][-nums[0]] = 2
        
        for i in range(len(nums)-1):
            # print("=================")
            # print(i)
            for key in dp[i]:
                if key+nums[i+1] in dp[i+1]:
                    dp[i+1][key+nums[i+1]] += dp[i][key]
                else:
                    dp[i+1][key+nums[i+1]] = dp[i][key]
                if key-nums[i+1] in dp[i+1]:
                    dp[i+1][key-nums[i+1]] += dp[i][key]
                else:
                    dp[i+1][key-nums[i+1]] = dp[i][key]
            # print(dp[i+1]) 
         
        if S in dp[-1]:
            return dp[-1][S]
        else:
            return 0
