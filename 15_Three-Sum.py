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


# Date: 2022-12-10, AC.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n =  len(nums)
        res = []

        for first in range(n):
            if first > 0 and nums[first] == nums[first-1]:
                continue 
            third = n-1
            target = -nums[first]

            for second in range(first+1, n):
                if second > first+1 and nums[second] == nums[second-1]:
                    continue 
                while second < third and nums[second]+nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second]+nums[third] == target:
                    res.append([nums[first], nums[second], nums[third]])

        return res        
        

# Exercise III:
# Dec 14, 2023
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_res = []
        nums = sorted(nums)
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            if nums[idx] > 0:
                continue
            residual_list = nums[:idx]+nums[idx+1:]
            left = 0 
            right = len(residual_list)-1
            while left < right:
                if residual_list[left]+residual_list[right] == -nums[idx]:
                    if sorted([residual_list[left], residual_list[right], nums[idx]]) not in final_res:
                        final_res.append(sorted([residual_list[left], residual_list[right], nums[idx]]))
                    left += 1
                elif residual_list[left]+residual_list[right] < -nums[idx]:
                    left += 1
                else:
                    right -= 1
        
        return final_res
