# Method I:
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1 for col in range(len(nums))]
        right = [1 for col in range(len(nums))]
        left[1] = nums[0]
        for i in range(2, len(left)):
            left[i] = left[i-1]*nums[i-1]
        right[len(right)-2] = nums[-1]
        for j in reversed(range(len(right)-2)):
            right[j] = right[j+1]*nums[j+1]
        res = []
        for index in range(len(nums)):
            res.append(left[index]*right[index])
        return res
            
 # Method II:
 class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for col in range(len(nums))]
        for i in reversed(range(len(nums)-1)):
            res[i] = res[i+1]*nums[i+1]
        left = 1
        for index in range(1, len(nums)):
            left = left*nums[index-1]
            right = res[index]
            res[index] = (left*right)
        return res
            
        
