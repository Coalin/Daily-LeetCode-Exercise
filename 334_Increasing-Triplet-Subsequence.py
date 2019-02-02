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
            
