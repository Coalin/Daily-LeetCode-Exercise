# 这题纠结的点在于...破外圈while循环所用的break位置.
# 24 ms, 99.68%.

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        
        m = len(matrix)
        n = len(matrix[0])
                
        res = []
        
        rowBegin = 0
        rowEnd = m-1
        colBegin = 0
        colEnd = n-1
        
        number = 1
        
        while number <= m*n:
            
            for i in range(colBegin, colEnd+1):
                res.append(matrix[rowBegin][i])
                number += 1
                if number > m*n:
                    break
            if number > m*n:
                break
            rowBegin += 1
            
            for j in range(rowBegin, rowEnd+1):
                res.append(matrix[j][colEnd])
                number += 1
                if number > m*n:
                    break
            if number > m*n:
                break
            colEnd -= 1
            
            for x in reversed(range(colBegin, colEnd+1)):
                res.append(matrix[rowEnd][x])
                number += 1
                if number > m*n:
                    break
            if number > m*n:
                break
            rowEnd -= 1
            
            for y in reversed(range(rowBegin, rowEnd+1)):
                res.append(matrix[y][colBegin])
                number += 1
                if number > m*n:
                    break
            if number > m*n:
                break
            colBegin += 1
            
        return res
        
        
