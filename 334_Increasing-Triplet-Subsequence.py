# Method I:
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        res = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j]+1)
        
        return max(res)>=3


# Method II:
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = [float('inf'), float('inf')]
        for num in nums:
            if num > res[1]:
                return True
            if num <= res[0]:
                res[0] = num
            else:
                res[1] = num
        
        return False
            

# Exercise III:
# June 17, 2023
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False 
        
        left_min = [nums[0] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            left_min[i] = min(left_min[i-1], nums[i])

        right_max = [nums[-1] for _ in range(len(nums))]
        for j in reversed(range(len(nums)-1)):
            right_max[j] = max(right_max[j+1], nums[j])

        for k in range(1, len(nums)-1):
            if left_min[k-1] < nums[k] and nums[k] < right_max[k+1]:
                return True 

        return False
