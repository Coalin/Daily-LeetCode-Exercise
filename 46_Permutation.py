class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 0 or len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            for rest in self.permute(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+rest)
        return res
        
        
