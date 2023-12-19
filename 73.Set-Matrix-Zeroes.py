# Exercise I:
# Dec 18, 2023
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag = set()
        col_flag = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_flag.add(i)
                    col_flag.add(j)

        for m in range(len(matrix)):
            for n in range(len(matrix[0])): 
                if m in row_flag or n in col_flag:
                    matrix[m][n] = 0
