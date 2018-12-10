class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res
        
    def dfs(self, matrix, i, j):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return 
        if matrix[i][j] == '1':
            matrix[i][j] = '0'
            self.dfs(matrix, i-1, j)
            self.dfs(matrix, i+1, j)
            self.dfs(matrix, i, j-1)
            self.dfs(matrix, i, j+1)
            
