class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0 
        right = sum(nums)-nums[0]
        i = 0

        while i < len(nums)-1:
            if left == right:
                return i
            else:
                left += nums[i]
                right -= nums[i+1]
                i += 1
        
        if sum(nums[:-1]) == 0:
            return len(nums)-1

        return -1
        