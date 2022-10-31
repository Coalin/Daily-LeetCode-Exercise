class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        final_res = 0
        while left < right:
            temp_res = min(height[left], height[right])*(right-left)
            final_res = max(final_res, temp_res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return final_res

# 33.15%; 120ms. 
        

# Exercise II: 20221031
class Solution:
    # 每个位置的容量始终受左右两端范围内(不是相邻)最高高度的的较低高度控制
    def trap(self, height: List[int]) -> int:
        res = 0 
        left_high = height[0]
        right_high = height[-1]
        for i in range(1, len(height)-1):
            left_high = max(left_high, height[i-1])
            right_high = max(height[i+1:])
            res += max((min(left_high, right_high)-height[i]), 0)
        return res
