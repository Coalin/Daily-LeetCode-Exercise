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
        
