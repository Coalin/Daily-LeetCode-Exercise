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
