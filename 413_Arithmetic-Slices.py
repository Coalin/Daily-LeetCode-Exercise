class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) < 3:
            return 0
        res = [0 for col in range(len(A))]
        if A[1]*2 == A[0]+A[2]:
            res[2] = 1
        for i in range(2, len(A)-1):
            if A[i]*2 == A[i-1]+A[i+1]:
                res[i+1] = res[i]+1
        return sum(res)
        
                
            
