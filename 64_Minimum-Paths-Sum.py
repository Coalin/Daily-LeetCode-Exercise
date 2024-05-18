class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for col in range(n)] for row in range(m)]
        if m < 1 or n < 1:
            return 0
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        for i in range(1,m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]


# Exercise II:
# Apr 8, 2024
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        dp[0][0] = grid[0][0]
        for col in range(1, len(grid[0])):
            dp[0][col] = dp[0][col-1] + grid[0][col]

        for row in range(1, len(grid)):
            dp[row][0] = dp[row-1][0] + grid[row][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1] 
