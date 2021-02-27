class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_mat = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_mat[j][i] = matrix[i][j]

        return new_mat
