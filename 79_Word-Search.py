class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) > len(board)*len(board[0]):
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    if self.dfs(board, word, i, j, 1):
                        return True
                    else:
                        board[i][j] = word[0]
                        
        return False
            
    def dfs(self, board, word, i, j, index):
        if index == len(word):
            return True
        
        if i-1 >= 0:
            if board[i-1][j] == word[index]:
                board[i-1][j] = '#'
                if self.dfs(board, word, i-1, j, index+1):
                    return True
                else:
                    board[i-1][j] = word[index]
                    
        if i+1 <= len(board)-1:
            if board[i+1][j] == word[index]:
                board[i+1][j] = '#'
                if self.dfs(board, word, i+1, j, index+1):
                    return True
                else:
                    board[i+1][j] = word[index]
                    
        if j-1 >= 0:
            if board[i][j-1] == word[index]:
                board[i][j-1] = '#'
                if self.dfs(board, word, i, j-1, index+1):
                    return True
                else:
                    board[i][j-1] = word[index]
                    
        if j+1 <= len(board[0])-1:
            if board[i][j+1] == word[index]:
                board[i][j+1] = '#'
                if self.dfs(board, word, i, j+1, index+1):
                    return True
                else:
                    board[i][j+1] = word[index]
                    
        return False
                        
        
        
