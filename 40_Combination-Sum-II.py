class Solution: 
    def __init__(self):
        self.res = []
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        self.dfs(candidates, target, [])
        return self.res
    
    def dfs(self, candidates, target, val_list):
        if target == 0:
            if val_list[:] not in self.res:
                self.res.append(val_list[:])
            return
        if target < 0:
            return
        if target > sum(candidates):
            return 
        for i in range(len(candidates)):
            val_list.append(candidates[i])
            self.dfs(candidates[i+1:], target-candidates[i], val_list)
            val_list.pop()
