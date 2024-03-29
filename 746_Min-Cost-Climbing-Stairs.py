class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
    
        res = [0, 0]
        for i in range(len(cost)):
            if i >= 2:
                cur_num = min(res[i-2]+cost[i-2], res[i-1]+cost[i-1])
                res.append(cur_num)
        return min(res[-2]+cost[-2], res[-1]+cost[-1])


# Exercise II
# Sep 28, 2023
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 1:
            return 0
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dispense_min = [2**32 for _ in range(len(cost))]
        dispense_min[0] = 0
        dispense_min[1] = 0
        
        for i in range(2, len(cost)):
            dispense_min[i] = min(dispense_min[i-1]+cost[i-1], dispense_min[i-2]+cost[i-2])
        return min(dispense_min[-1]+cost[-1], dispense_min[-2]+cost[-2])
