# 遍历
# 总利润：把每两天的价格增长量加起来
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) >= 2:
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    res += prices[i]-prices[i-1]
        return res


# 动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        if len(prices) >= 2:
            for i in range(1, len(prices)):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        return dp[-1][0]


# Exercise III:
# Feb 23, 2023
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]

        # without stock in hand
        dp[0][0] = 0 
        # with stock in hand
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            # without stock in hand
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            # with stock in hand
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        return dp[-1][0]
