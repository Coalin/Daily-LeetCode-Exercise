class Solution:
    def tribonacci(self, n: int) -> int:
        res = []
        res.append(0)
        res.append(1)
        res.append(1)

        if n == 0:
            return 0 
        if n == 1:
            return 1 
        if n == 2:
            return 1

        for i in range(3, n+1):
            res.append(res[i-3]+res[i-2]+res[i-1])

        return res[-1]
