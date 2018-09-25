class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return 0
        dp = [[0 for col in range(n)] for row in range(m)]
        # dp = [[0]*n]*m
        for i in xrange(m):
            dp[i][0] = 1
        for j in xrange(n):
            dp[0][j] = 1
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

# 95.75%; 44ms. 
    
                
        
