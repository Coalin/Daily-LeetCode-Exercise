class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        left = 0
        right = l-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
                break
        if target > nums[left]:
            return left+1
        else:
            return left


# Exercise II:
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1

        while left < right:
            mid = left + (right-left)//2

            if nums[left] == target:
                return left 
            if nums[right] == target:
                return right 
            if nums[mid] == target:
                return mid 

            if nums[mid] < target:
                left = mid+1 
            else:
                right = mid-1 

        if nums[left] < target:
            return left+1
        else:
            return left

