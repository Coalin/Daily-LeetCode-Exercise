class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                count += 1
        for j in range(count):
            nums.remove(0)
        nums += [0]*count 


# Exercise II:
# Apr 15, 2023
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0

        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1

        while i < len(nums):
            nums[i] = 0
            i += 1
