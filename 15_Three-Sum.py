# Actually, this solution is to be finished because it is out of time limits.
# The time complexity is n^2, which is still rejected by Leetcode.
# Date: 2018-08-13.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
#        if len(nums) == 3:
#            if nums[0]+nums[1]+nums[2]==0:
#                return [nums]
#            else:
#                return []
        res = []
        res_final = []
        nums = sorted(nums)
        for i in range(len(nums)):
            nums_clean = nums[:i]+nums[i+1:]
            res += self.twoSum(nums_clean, -nums[i])
#            if result:
#                for item in result:
#                    l = item[0]
#                    r = item[1]
#                    res.append(sorted([nums[i], l, r]))
        for j in res:
            j = sorted(j)
            if j not in res_final:
                res_final.append(j)
        return res_final
            
        
    def twoSum(self, nums, target):
        left = 0
        right = len(nums)-1
        res_middle = []
        while left < right:
            if nums[left] + nums[right] == target:
                res_middle.append([-target, nums[left],nums[right]])
                left += 1
                right -= 1
            if nums[left] + nums[right] < target:
                left += 1
            if nums[left] + nums[right] > target:
                right -= 1
        return res_middle

        
        
        
