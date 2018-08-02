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

        
                
            
        
