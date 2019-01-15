class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        last = copy.deepcopy(board)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur_count = self.findCount(last, i, j)
                print(cur_count)
                if board[i][j] == 1:
                    if cur_count < 2 or cur_count > 3:
                        board[i][j] = 0
                else:
                    if cur_count == 3:
                        board[i][j] = 1
                        
    def findCount(self, board, i, j):
        count = 0
        
        if len(board) == 1 and len(board[0]) == 1:
            return 0
        if len(board[0]) == 1:
            try:
                count += board[i][j-1]
            except:
                pass
            try:
                count += board[i][j+1]
            except:
                pass
            return count
        if len(board) == 1:
            try:
                count += board[i-1][j]
            except:
                pass
            try:
                count += board[i+1][j]
            except:
                pass
            return count 
        
        if i > 0 and i < len(board)-1 and j > 0 and j < len(board[0])-1:
            count += board[i-1][j] 
            count += board[i-1][j-1] 
            count += board[i-1][j+1]
            count += board[i][j-1]
            count += board[i][j+1]
            count += board[i+1][j-1]
            count += board[i+1][j]
            count += board[i+1][j+1]
            return count
        if i == 0 and j == 0:
            count += board[i][j+1]
            count += board[i+1][j]
            count += board[i+1][j+1]
            return count 
        if i == 0 and j == len(board[0])-1:
            count += board[i][j-1]
            count += board[i+1][j]
            count += board[i+1][j-1]
            return count
        if i == len(board)-1 and j == 0:
            count += board[i][j+1]
            count += board[i-1][j]
            count += board[i-1][j+1]
            return count
        if i == len(board)-1 and j == len(board[0])-1:
            count += board[i][j-1]
            count += board[i-1][j]
            count += board[i-1][j-1]
            return count
        if i == 0:
            count += board[i][j-1]
            count += board[i][j+1]
            count += board[i+1][j]
            count += board[i+1][j-1]
            count += board[i+1][j+1]
            return count 
        if i == len(board)-1:
            count += board[i][j-1]
            count += board[i][j+1]
            count += board[i-1][j]
            count += board[i-1][j-1]
            count += board[i-1][j+1]
            return count  
        if j == 0:
            count += board[i-1][j]
            count += board[i+1][j]
            count += board[i-1][j+1]
            count += board[i][j+1]
            count += board[i+1][j+1]
            return count   
        if j == len(board[0])-1:
            count += board[i-1][j]
            count += board[i+1][j]
            count += board[i-1][j-1]
            count += board[i][j-1]
            count += board[i+1][j-1]
            return count             
            



        
