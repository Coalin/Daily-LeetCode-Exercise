from math import pow

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2:
            return 0
        res = 0
        
        for i in range(len(points)):
            distance_hash = dict()
            
            for j in range(len(points)):
                if j != i:
                    length = pow(points[i][0]-points[j][0], 2) + pow(points[i][1]-points[j][1], 2)
                    if length in distance_hash:
                        distance_hash[length].append(j)
                    else:
                        distance_hash[length] = [j]

            for x in distance_hash:
                if len(distance_hash[x]) == 2:
                    res += 2
                elif len(distance_hash[x]) > 2:
                    res += len(distance_hash[x])*(len(distance_hash[x])-1)
            
        return res
                    
            
                
        
