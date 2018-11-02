# 这一题一开始跑出现了BUG，原因是最后一个for循环变量名设为n与函数的参数冲突了，醉了...
# 28 ms, 98.05%.

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[-1 for col in range(n)] for row in range(n)]
        
        rowBegin = 0
        rowEnd = n-1
        colBegin = 0
        colEnd = n-1
        
        number = 1
        
        while number <= n**2:
            for i in range(colBegin, colEnd+1):
                res[rowBegin][i] = number
                number += 1
            rowBegin += 1
            
            for j in range(rowBegin, rowEnd+1):
                res[j][colEnd] = number
                number += 1
            colEnd -= 1
            
            for x in reversed(range(colBegin, colEnd+1)):
                res[rowEnd][x] = number
                number += 1
            rowEnd -= 1
            
            for y in reversed(range(rowBegin, rowEnd+1)):
                res[y][colBegin] = number
                number += 1
            colBegin += 1
            
        return res
            
