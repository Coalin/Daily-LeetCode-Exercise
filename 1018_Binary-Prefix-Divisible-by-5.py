class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        cur_str = ''
        for i in range(len(A)):
            cur_str += str(A[i])
            if int(cur_str, 2)%5 == 0:
                res.append(True)
            else:
                res.append(False) 
        return res
        