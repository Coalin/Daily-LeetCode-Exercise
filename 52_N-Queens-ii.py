class Solution:
    def __init__(self):
        self.column = set()
        self.diagram1 = set()
        self.diagram2 = set()
    
    def backTrack(self, row, n):
        if row == n:
            return 1 
        else:
            cnt = 0
            for col in range(n):
                if col in self.column or row-col in self.diagram1 or row+col in self.diagram2:
                    continue 
                self.column.add(col)
                self.diagram1.add(row-col)
                self.diagram2.add(row+col) 
                cnt += self.backTrack(row+1, n)
                self.column.remove(col)
                self.diagram1.remove(row-col)
                self.diagram2.remove(row+col)              
        return cnt 

    def totalNQueens(self, n: int) -> int:
        return self.backTrack(0, n)
