class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        last = prices[0]
        res = 0
        for i in prices:
            if i > last:
                res += i-last
            last = i
        return res
        
# 总利润：把每两天的价格增长量加起来

# Exercise II
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i]-prices[i-1], 0)
        return res
