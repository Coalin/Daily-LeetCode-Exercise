class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [[0 for col in range(row+1)] for row in range(n)]
        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
        for i in range(n-2, -1, -1):
            for j in range(i+1):    
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]
