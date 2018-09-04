class Solution(object):
    def permuteUnique(self, nums):
        res = self.permuteUnique_(nums)
        res_final = []
        for item in res:
            if item not in res_final:
                res_final.append(item)
        return res_final
            
    def permuteUnique_(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            for rest in self.permuteUnique_(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+rest)
        return res
