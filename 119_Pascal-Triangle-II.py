# Original Method: Out of Time Limit

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            result = [1]
        elif rowIndex == 1:
            result = [1, 1]
        else:
            result = [1] * (rowIndex+1)
            for i in range(1, rowIndex):
                result[i] = self.getRow(rowIndex-1)[i-1]+self.getRow(rowIndex-1)[i]
        return result 
        
        
 # Method Accepted
 
 class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        elif rowIndex > 1:
            currow = [1, 1]
            for i in range(2, rowIndex+2):
                prerow = currow
                currow = [1]
                for j in range(1, i-1):
                    currow.append(prerow[j-1]+prerow[j])
                currow.append(1)
        return currow
