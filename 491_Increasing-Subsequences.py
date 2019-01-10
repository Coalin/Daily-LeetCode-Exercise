class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(nums, 0, [])
        return self.res
        
    def dfs(self, nums, index, path):
        if len(path) >= 2 and path not in self.res:
            self.res.append(copy.deepcopy(path))
        for i in range(index, len(nums)):
            if not path or path[-1] <= nums[i]:
                path += [nums[i]]
                self.dfs(nums, i+1, path)
                if path:
                    path.pop()
        
        

            
        
