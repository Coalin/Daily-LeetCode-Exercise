class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [0] + [float('inf')]*T
        # 遍历每一个阈值
        for i in range(1, T + 1):
            # 轮寻每一个片段，寻找最小值
            for aj, bj in clips:
                if i > aj and i <= bj:
                    dp[i] = min(dp[i], dp[aj]+1)
        return -1 if dp[-1] == float('inf') else dp[-1]
