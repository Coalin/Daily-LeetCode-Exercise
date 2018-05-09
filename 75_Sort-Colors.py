class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = j = k = 0
        for i in nums:
            if i == 0:
                n += 1
            elif i == 1:
                j += 1
            else:
                k += 1
        for i in range(len(nums)):
            if i < n:
                nums[i] = 0
            elif i >= n+j:
                nums[i] = 2
            else:
                nums[i] = 1
