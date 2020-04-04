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
