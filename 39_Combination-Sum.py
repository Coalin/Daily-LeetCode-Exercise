class Solution:
    def __init__(self):
        self.res = []
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.dfs(candidates, target, 0, [])
        return self.res
    
    def dfs(self, candidates, target, start, val_list):
        if target == 0:
            self.res.append(val_list[:])
            return 
        if target < 0:
            return 
        for i in range(start, len(candidates)):
            val_list.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i, val_list)
            val_list.pop()
