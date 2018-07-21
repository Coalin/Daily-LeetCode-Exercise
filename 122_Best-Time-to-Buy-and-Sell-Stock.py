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
