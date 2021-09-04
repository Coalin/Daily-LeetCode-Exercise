class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0 
        if n == 1:
            return 1 

        MOD = 1e9+7
        res = [0 for _ in range(n+1)]
        res[0] = 0
        res[1] = 1

        for i in range(2, n+1):
            res[i] = res[i-1]%MOD+res[i-2]%MOD 
        return int(res[i]%MOD)
