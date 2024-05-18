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
                

# Exercise II:
# Feb 18, 2023
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n  = len(obstacleGrid[0])

        dp = [[1 for _ in range(n)] for _ in range(m)]

        for x in range(m):
            for y in range(n):
                if obstacleGrid[x][y] == 1:
                    dp[x][y] = 0

        for p in range(1, m):
            if obstacleGrid[p][0] != 1:
                dp[p][0] = dp[p-1][0]

        for q in range(1, n):
            if obstacleGrid[0][q] != 1:
                dp[0][q] = dp[0][q-1]
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]
    

# Exercise III:
# Apr 9, 2024
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for x in range(1, m):
            dp[x][0] = dp[x-1][0]
            if obstacleGrid[x][0] == 1:
                dp[x][0] = 0 

        for y in range(1, n):
            dp[0][y] = dp[0][y-1]
            if obstacleGrid[0][y] == 1:
                dp[0][y] = 0 

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0

        return dp[-1][-1]
