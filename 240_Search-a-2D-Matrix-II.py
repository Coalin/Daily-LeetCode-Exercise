class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False
        
        left = up = 0
        right = len(matrix[0])-1
        down = len(matrix)-1
        
        for i in range(len(matrix[0])):
            if matrix[0][i] > target:
                right = i-1
                break
        for j in range(len(matrix)):
            if matrix[j][0] > target:
                down = j-1
                break
        
        for x in range(down+1):
            for y in range(right+1):
                if matrix[x][y] == target:
                    return True
                if matrix[x][y] > target:
                    break
        
        return False
        
        
