class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix) == 1:
            for item in range(len(matrix[0])):
                if matrix[0][item] == target:
                    return True
        if len(matrix[0]) == 1:
            for index in range(len(matrix)):
                if matrix[index][0] == target:
                    return True
        if len(matrix) == 2:
            for item in range(len(matrix[0])):
                if matrix[0][item] == target:
                    return True
                if matrix[1][item] == target:
                    return True
        if len(matrix[0]) == 2:
            for index in range(len(matrix)):
                if matrix[index][0] == target:
                    return True
                if matrix[index][1] == target:
                    return True
        left = 0
        right = len(matrix)-1
        while left+1 < right:
            middle = int((left+right)/2)
            if matrix[middle][0] < target:
                left = middle
            elif matrix[middle][0] > target:
                right = middle
            else:
                break
        for i in range(left, right+1):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
            
   # Rank: 100%


# Exercise II:
# Jan 24, 2024
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False 

        left = 0 
        right = len(matrix)*len(matrix[0])-1 

        while left <= right:
            mid = left + (right-left)//2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1 
            else:
                right = mid - 1

        return False
