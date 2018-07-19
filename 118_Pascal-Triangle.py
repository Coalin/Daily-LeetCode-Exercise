class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            res = []
        elif numRows == 1:
            res = [[1]]
        elif numRows == 2:
            res = [[1], [1,1]]
        else:
            res = [[1], [1,1]]
            for i in range(2, numRows):
                row = [1]
                for j in range(1, i):
                
                # Pay attention to: 
                # [1] The above i in iteration: rather than numRows
                # [2] List.append(): rather than direct "="
                
                    num = res[i - 1][j - 1] + res[i - 1][j]
                    row.append(num)
                row.append(1)
                res.append(row)
        return res
        
