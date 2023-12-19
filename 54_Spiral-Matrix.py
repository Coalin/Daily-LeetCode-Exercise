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
    
# Exercise II
# Mar 19, 2019
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:              
        def cycle(row, col, ri, ci, case):
            if row == 0 or col == 0:
                return 
            
            if case == 0:
                for i in range(ci, ci+col):
                    res.append(matrix[ri][i])
                ri += 1
                ci = ci+col-1
                row -= 1
                case = (case+1)%4
                cycle(row, col, ri, ci, case)
                
            elif case == 1:
                for i in range(ri, ri+row):
                    res.append(matrix[i][ci])
                ri = ri+row-1
                ci -= 1
                col -= 1
                case = (case+1)%4
                cycle(row, col, ri, ci, case)
                
            elif case == 2:
                for i in reversed(range(ci-col+1, ci+1)):
                    res.append(matrix[ri][i])
                ri -= 1
                ci = ci-col+1
                row -= 1
                case = (case+1)%4
                cycle(row, col, ri, ci, case)

            elif case == 3:
                for i in reversed(range(ri-row+1, ri+1)):
                    res.append(matrix[i][ci])
                ri = ri-row+1
                ci += 1
                col -= 1
                case = (case+1)%4
                cycle(row, col, ri, ci, case)
        
        if not matrix:
            return []
        res = []
        cycle(len(matrix), len(matrix[0]), 0, 0, 0)
        return res
        

# Exercise III:
# Dec 17, 2023
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        m = len(matrix)
        n = len(matrix[0])

        row_begin = 0 
        row_end = m-1 
        col_begin = 0 
        col_end = n-1

        number = 0

        while number < m*n:
            for j in range(col_begin, col_end+1):
                res.append(matrix[row_begin][j])
                number += 1
                if number >= m*n:
                    break
            if number >= m*n:
                break
            row_begin += 1

            for i in range(row_begin, row_end+1):
                res.append(matrix[i][col_end])
                number += 1
                if number >= m*n:
                    break
            if number >= m*n:
                break
            col_end -= 1

            for p in reversed(range(col_begin, col_end+1)):
                res.append(matrix[row_end][p])
                number += 1
                if number >= m*n:
                    break
            if number >= m*n:
                break
            row_end -= 1

            for q in reversed(range(row_begin, row_end+1)):
                res.append(matrix[q][col_begin])  
                number += 1 
                if number >= m*n:
                    break
            if number >= m*n:
                break
            col_begin += 1

        return res
