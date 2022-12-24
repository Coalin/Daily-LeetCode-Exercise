class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = 2**32-1
        res_list = []
        for i in range(len(nums)):
            new_target = target-nums[i]
            new_nums = nums[:i]+nums[i+1:]
            left = 0
            right = len(new_nums)-1
            while left<right:
                if abs(new_nums[left]+new_nums[right]-new_target)<res:
                    res = abs(new_nums[left]+new_nums[right]-new_target)
                    res_list = [nums[i], new_nums[left], new_nums[right]]
                if new_nums[left]+new_nums[right] < new_target:
                    left += 1
                elif new_nums[left]+new_nums[right] > new_target:
                    right -= 1
                else:
                    return sum([nums[i], new_nums[left], new_nums[right]])
        return sum(res_list)
                    
        
# Exercise 20200229
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None
        nums = sorted(nums)         
        res = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            cur_sum = nums[i]+self.twoSumClosest(nums[:i]+nums[i+1:], target-nums[i])
            if abs(cur_sum-target) <  abs(res-target):
                res = cur_sum 
            print(nums[i], cur_sum)
        return res
            
    def twoSumClosest(self, nums, target):
        left = 0 
        right = len(nums)-1
        res_sum = nums[0]+nums[-1]
        gap = abs(res_sum-target)
        while left < right:
            if nums[left]+nums[right] == target:
                return target
            else:
                cur_gap = abs(nums[left]+nums[right] - target)
                if cur_gap < gap:
                    res_sum = nums[left]+nums[right]
                    gap = cur_gap 
                if nums[left]+nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return res_sum 


# Exercise 20221217
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n =  len(nums)
        res = []
        print(nums)
        best = 2**32-1

        for first in range(n):
            if first > 0 and nums[first] == nums[first-1]:
                continue 

            second = first+1
            third = n-1

            while second < third:
                total = nums[first]+nums[second]+nums[third] 
                if total == target: 
                    return target
                if abs(total-target) < abs(best-target):
                    best = total 
                if total > target:
                    third_0 = third-1 
                    while third_0-1 > second and nums[third_0-1] == nums[third_0]:
                        third_0 -= 1
                    third = third_0 
                else:
                    second_0 = second+1
                    while second_0+1 < third and nums[second_0+1] == nums[second+0]:
                        second_0 += 1
                    second = second_0

        return best