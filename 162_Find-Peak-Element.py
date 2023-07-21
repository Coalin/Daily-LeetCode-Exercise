# Exercise I:
# July 22, 2023

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')]+nums+[float('-inf')]
        left = 0 
        right = len(nums)-1
        res = -1 

        while left < right:
            mid = left+(right-left)//2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                res = mid 
                break
            elif nums[mid-1] >= nums[mid]:
                right = mid 
            elif nums[mid] <= nums[mid+1]:
                left = mid 

        return res-1
