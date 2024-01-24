# Exercise I:
# Jan 24, 2024
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums)-1
        res = -1 

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                res = mid 
                break 
            if nums[left] == target:
                res = left 
                break 
            if nums[right] == target:
                res = right 
                break
            elif nums[mid] > target:
                right = mid - 1 
            else:
                left = mid + 1

        if res == -1:
            return [-1, -1]

        l = r = res
        
        while l >= 0 and nums[l] == target:
                l -= 1
        while r <= len(nums)-1 and nums[r] == target:
                r += 1
        
        return [l+1, r-1]

