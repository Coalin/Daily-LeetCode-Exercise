# Attempt I: 贪心的思路，方法错。维护一个静态dict不能保证每次remove后余下的序列仍保持有序。
# class Solution:
#     def findMinArrowShots(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
#         left = 10000 
#         right = -10000
#         for i in range(len(points)):
#             left = min(left, points[i][0])
#             right = max(right, points[i][1])
        
#         poi_dic = dict()
#         poi_dic_len = dict()
        
#         count = 0
        
#         for j in range(len(points)):
#             for x in range(points[j][0], points[j][1]+1):
#                 if x in poi_dic:
#                     poi_dic[x].append(points[j])
#                 else:
#                     poi_dic[x] = [points[j]]
                    
#         for key in poi_dic:
#             poi_dic_len[key] = len(poi_dic[key])
            
#         arror = self.sort_by_value(poi_dic_len)
#         print(arror)
        
#         for y in arror:
#             if not points:
#                 return count
#             intersect = False
#             for n in points:
#                 if n in poi_dic[y]:
#                     intersect = True
#                     break
#             if intersect:
#                 count += 1
#                 for m in poi_dic[y]:
#                     try:
#                         points.remove(m)
#                     except:
#                         pass
                    
#     def sort_by_value(self, d):
#         items=d.items()
#         backitems=[[v[1], v[0]] for v in items]
#         backitems = sorted(backitems, reverse=True)
#         return [backitems[i][1] for i in range(len(backitems))]


# Attempt II：AC
class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points = sorted(points, key=lambda Interval: Interval[0])
        
        count = 1
        ref = points[0]
        
        for i in range(1, len(points)):
            if points[i][0] > ref[1]:
                count += 1
                ref = points[i]
            else:
                if points[i][1] < ref[1]:
                    ref = [points[i][0], points[i][1]]
        
        return count
            
        


        
        
            
        
