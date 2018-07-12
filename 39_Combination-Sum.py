class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        def dfs(candidates, target, start, path, res):
            if target == 0:
                return res.append(path+[])
                
            for i in range(start, len(candidates)):
                if target-candidates[i] >= 0:
                    path.append(candidates[i])
                    dfs(candidates, target-candidates[i], i, path, res)
                    path.pop()
                    
        res = []
        dfs(candidates, target, 0, [], res)
        return res
