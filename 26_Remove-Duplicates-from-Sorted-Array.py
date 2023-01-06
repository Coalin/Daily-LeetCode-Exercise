class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ind = 0
        for i in range(len(nums)):
            if nums[i] != nums[ind]:
                ind += 1
                nums[ind] = nums[i]
        return ind+1
      
# 98.99%; 56ms.
                

# Exercise II:
# Jan 7, 2023
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        j = 1

        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
            
        return i+1        
