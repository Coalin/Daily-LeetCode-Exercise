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


# Exercise III:
# Mar 19, 2024
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        k = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k 
