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
            

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.infect(grid, i, j)
                    res += 1
        return res 

    def infect(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
           return 
        grid[i][j] = '2' 
        self.infect(grid, i-1, j)
        self.infect(grid, i+1, j)
        self.infect(grid, i, j-1)
        self.infect(grid, i, j+1)


# Exercise III:
# Apr 3, 2023
class Solution:
    def dfs(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return 

        grid[x][y] = '0'
        self.dfs(grid, x-1, y)
        self.dfs(grid, x+1, y)
        self.dfs(grid, x, y-1)
        self.dfs(grid, x, y+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)

        return res


# Exercise IV:
# June 23, 2024
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, x, y):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1 or grid[x][y] != '1':
                return 
            grid[x][y] = '0'
            dfs(grid, x-1, y)
            dfs(grid, x+1, y)
            dfs(grid, x, y-1)
            dfs(grid, x, y+1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(grid, i, j)

        return cnt
