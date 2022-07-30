class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 我们目前持有一支股票
        has_stock = [0 for _ in range(len(prices))]
        # 我们目前不持有任何股票，并且期末不处于冷冻期中
        no_stock = [0 for _ in range(len(prices))]
        # 我们目前不持有任何股票，并且期末处于冷冻期中
        no_stock_cold = [0 for _ in range(len(prices))]

        has_stock[0] = -prices[0]
        no_stock[0] = 0
        no_stock_cold[0] = 0

        for i in range(1, len(prices)):
            has_stock[i] = max(has_stock[i-1], no_stock[i-1]-prices[i])
            no_stock[i] = max(no_stock[i-1], no_stock_cold[i-1])
            no_stock_cold[i] = has_stock[i-1]+prices[i]

        return max(no_stock[-1], no_stock_cold[-1])
