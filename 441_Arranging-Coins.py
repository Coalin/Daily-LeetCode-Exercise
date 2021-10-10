class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 1 
        # 1 2 = 3 
        # 1 2 3 = 6 
        # S = 1+2+...+n=(1+n)*n/2
        # n**2+n-2S=0
        return int((-1+sqrt(1+8*n))/2)


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n 
        while left < right:
            mid = left+(right-left+1)//2
            if (1+mid)*mid/2 <= n:
                left = mid 
            else:
                right = mid-1 
        return left 
