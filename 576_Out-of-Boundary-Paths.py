class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # dp[i][j][k] 运动i次之后在[j][k]的路径数
        MOD = 10**9+7
        # 初始化dp，注意maxMove+1
        dp = [[[0]*n for _ in range(m)] for _ in range(maxMove+1)]
        # 起始步
        dp[0][startRow][startColumn] = 1 
        res = 0 
        for i in range(maxMove):
            for j in range(m):
                for k in range(n):
                    if dp[i][j][k] > 0:
                        for j1, k1 in [(j-1, k), (j+1, k), (j, k-1), (j, k+1)]:
                            # 如果没出界
                            if j1 < m and j1 >= 0 and k1 < n and k1 >= 0:
                                dp[i+1][j1][k1] = (dp[i+1][j1][k1]+dp[i][j][k])%MOD
                            # 如果出界了
                            else:
                                res = (res+dp[i][j][k])%MOD
        return res 
