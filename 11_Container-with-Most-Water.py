class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left = 0
        right = len(height)-1
        while left < right:
            water = min(height[left], height[right]) * (right-left)
            if water > max_water:
                max_water = water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
        
