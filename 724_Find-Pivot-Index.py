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
        

# Exercise II:
# May 5, 2023
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0 
        total_sum = sum(nums)

        if left_sum == total_sum-left_sum-nums[0]:
            return 0

        for i in range(1, len(nums)):
            left_sum += nums[i-1]
            right_sum = total_sum-left_sum-nums[i]
            if left_sum == right_sum:
                return i 

        return -1
