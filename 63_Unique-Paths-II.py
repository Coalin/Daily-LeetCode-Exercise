class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        dp = [[0 for col in range(n)] for row in range(m)]
        dp[0][0] = 1
        for i in xrange(1, m):
            if obstacleGrid[i-1][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
        for j in xrange(1, n):
            if obstacleGrid[0][j-1] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]
        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i-1][j]==0 and obstacleGrid[i][j-1]==0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif obstacleGrid[i-1][j]==0 and obstacleGrid[i][j-1]==1:
                    dp[i][j] = dp[i-1][j]
                elif obstacleGrid[i-1][j]==1 and obstacleGrid[i][j-1]==0:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[m-1][n-1]
                    
