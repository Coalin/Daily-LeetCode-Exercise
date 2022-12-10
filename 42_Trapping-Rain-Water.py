class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        max_height = 0 
        max_height_index = 0

        for i in range(len(height)):
            if height[i] > max_height:
                max_height = height[i]
                max_height_index = i 

        water_left = 0 
        tmp_height_left = height[0]
        for i in range(1, max_height_index):
            if height[i] > tmp_height_left:
                tmp_height_left = height[i]
            else:
                water_left += (tmp_height_left-height[i])
        
        water_right = 0
        tmp_height_right = height[-1]
        for j in reversed(range(max_height_index+1, len(height))):
            if height[j] > tmp_height_right:
                tmp_height_right = height[j]
            else:
                water_right += (tmp_height_right-height[j])

        return water_left+water_right


# Exercise II: 20221022
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
