class Solution:    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0 or len(board[0]) == 0:
            return
        
        for m in range(len(board)):
            if board[m][0] == 'O':
                self.dfs(board, m, 0)
            if board[m][len(board[0]) - 1] == 'O':
                self.dfs(board, m, len(board[0]) - 1)

        for n in range(1, len(board[0]) - 1):
            if board[0][n] == 'O':
                self.dfs(board, 0, n)
            if board[len(board) - 1][n] == 'O':
                self.dfs(board, len(board) - 1, n)

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                if board[x][y] == '*':
                    board[x][y] = 'O'
                
                
    def dfs(self, board, i, j):
        if board[i][j] != 'X':
            board[i][j] = '*'
            if i - 1 >= 0:
                if board[i-1][j] == 'O':
                    self.dfs(board, i - 1, j)
            if i + 1 <= len(board) - 1:
                if board[i+1][j] == 'O':
                    self.dfs(board, i + 1, j)
            if j - 1 >= 0:
                if board[i][j-1] == 'O':
                    self.dfs(board, i, j - 1)
            if j + 1 <= len(board[0]) - 1:
                if board[i][j+1] == 'O':
                    self.dfs(board, i, j + 1)


# Exercise III:
# Apr 3, 2023
class Solution:
    def dfs(self, board, x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != 'O':
            return 
        
        board[x][y] = '1'
        
        self.dfs(board, x-1, y)
        self.dfs(board, x+1, y)
        self.dfs(board, x, y-1)
        self.dfs(board, x, y+1)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for j in range(len(board[0])):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[-1][j] == 'O':
                self.dfs(board, len(board)-1, j)    

        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][-1] == 'O':
                self.dfs(board, i, len(board[0])-1) 

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        
# Exercise IV:
# June 23, 2024
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, x, y):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != 'O':
                return 
            
            board[x][y] = '1'
            
            dfs(board, x-1, y)
            dfs(board, x+1, y)
            dfs(board, x, y-1)
            dfs(board, x, y+1)

        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(board, i, 0)
            if board[i][-1] == 'O':
                dfs(board, i, len(board[0])-1) 

        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(board, 0, j)
            if board[-1][j] == 'O':
                dfs(board, len(board)-1, j)    

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
