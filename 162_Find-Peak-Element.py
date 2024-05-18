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
            if nums[mid-1] > nums[mid]:
                right = mid 
            else:
                left = mid 

        return res-1


# Exercise II:
# Jan 24, 2024
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')]+nums+[float('-inf')]
        left = 0 
        right = len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid-1 
            elif nums[mid] < nums[mid-1]:
                right = mid
            else:
                left = mid

        return left-1
