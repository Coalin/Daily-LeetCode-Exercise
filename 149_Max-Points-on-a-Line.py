# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from fractions import Fraction

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        if len(points) == 1:
            return 1
        
        res_dic = {}
        
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                if points[i].x != points[j].x and points[i].y != points[j].y:
                    if points[i].x-points[j].x != 0:
                        cur_a = Fraction((points[i].y - points[j].y), (points[i].x - points[j].x))
                        cur_b = Fraction(points[i].y - cur_a * points[i].x)
                        cur_res = str(cur_a._numerator) + '/' + str(cur_a._denominator) + '_' + str(cur_b._numerator) + '/' +str(cur_b._numerator)
                    else:
                        cur_res = 'x_'+str(points[i].x)
                else:
                    cur_res = str(points[i].x)+'__'+str(points[i].y)
                if cur_res in res_dic:
                    if i not in res_dic[cur_res]:
                        res_dic[cur_res].append(i)
                    if j not in res_dic[cur_res]:
                        res_dic[cur_res].append(j)
                else:
                    res_dic[cur_res] = [i, j]
        res = 0
        for index in res_dic:
            res = max(len(res_dic[index]), res)
        return res
            
            
        
        
