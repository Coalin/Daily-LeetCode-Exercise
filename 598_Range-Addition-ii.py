class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        row = m 
        col = n 
        for lst in ops:
            row = min(row, lst[0])
            col = min(col, lst[1])
        return row*col
