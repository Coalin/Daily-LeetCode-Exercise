# Method I：
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if not z:
            return True
        if x+y<z:
            return False

        small = min(x, y)
        big = max(x, y)

        if small == 0:
            return big == z

        while big%small != 0:
            big, small = small, big%small 
            
        return z%small == 0
        
        
# Method II:
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        stack = [(0, 0)]
        seen = set()
        while stack:
            (remain_x, remain_y) = stack.pop()
            if remain_x == z or remain_y == z or remain_x+remain_y == z:
                return True
            if (remain_x, remain_y) in seen:
                continue 
            seen.add((remain_x, remain_y))
            stack.append((0, remain_y))
            stack.append((remain_x, 0))
            stack.append((x, remain_y))
            stack.append((remain_x, y))
            if remain_x > y-remain_y:
                stack.append((remain_x-(y-remain_y), y))
            else:
                stack.append((0, remain_x+remain_y))
            if remain_y > x-remain_x:
                stack.append((x, remain_y-(x-remain_x)))
            else:
                stack.append((remain_x+remain_y, 0))
        return False
