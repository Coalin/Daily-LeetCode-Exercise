import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area == 0 or area != int(area):
            return None
        
        length = math.sqrt(area)
        if length == int(length):
            return [int(length), int(length)]
        
        w = round(length)
        # print(w)
        while w > 0:
            if area%w == 0:
                # print('flag')
                return [area//w, w]
            else:
                w -= 1


# 20211023 Exercise 
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(sqrt(area)), 0, -1):
            if area%i == 0:
                return [area//i, i]
