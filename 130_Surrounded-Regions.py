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


    
            
        
