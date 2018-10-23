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
                    
        
