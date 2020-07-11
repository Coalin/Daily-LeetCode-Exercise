class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        res = 0
        minprice = prices[0]
        for i in prices:
            curres = i - minprice
            if i < minprice:
                minprice = i
            res = max(res, curres)
        return res

# Exercise II:
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        final_res = 0
        cur_min = prices[0]

        for i in range(1, len(prices)):
            final_res = max(prices[i]-cur_min, final_res)
            cur_min = min(cur_min, prices[i])
        
        return final_res

# Solution II: DP
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])

        return dp[-1][0]
