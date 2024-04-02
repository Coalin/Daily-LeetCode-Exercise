# Exercise I:
# Apr 2, 2024
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_sum = 0 
        total_sum = 0 
        start = 0

        for i in range(len(gas)):
            cur_sum += gas[i]-cost[i]
            total_sum += gas[i]-cost[i]

            if cur_sum < 0:
                cur_sum = 0 
                start = i+1

        if total_sum < 0:
            return -1 
        else:
            return start
