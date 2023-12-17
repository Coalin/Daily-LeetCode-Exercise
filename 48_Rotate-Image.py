# Exercise I:
# Dec 17, 2023

import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix_cp = copy.deepcopy(matrix)

        for i in range(n):
            for j in range(n):
                matrix[j][n-i-1] = matrix_cp[i][j]


# Exercise II:
# Dec 17, 2023
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i] = matrix[i][::-1]
