class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [0 for col in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]


# Exercise II:
# Jan 9, 2023
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        res = []
        res.append(1)
        res.append(2)

        for _ in range(3, n+1):
            res.append(res[-2]+res[-1])

        return res[-1]
