class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        left = 0
        right = l-1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            # 左边有序
            if nums[mid] >= nums[left]: 
                if target > nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1                   
            # 右边有序
            else: 
                if target < nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
                    
                
            
                
            
