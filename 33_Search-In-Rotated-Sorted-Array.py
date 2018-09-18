class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = left + (right-left)//2
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[middle] == target:
                return middle
            if nums[left] < nums[middle]:
                if target > nums[left] and target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if target > nums[middle] and target < nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1
    
# 92.02%; 48ms.
