# Exercise I:
# Jan 28, 2024
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i-coin]+1, dp[i])

        return -1 if dp[-1] == amount+1 else dp[-1]
                