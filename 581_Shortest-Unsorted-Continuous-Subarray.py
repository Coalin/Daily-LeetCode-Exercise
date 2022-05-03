class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        left = 0 
        right = len(nums)-1

        while left < right-1:
            cur_min = min(nums[left:right+1])
            cur_max = max(nums[left:right+1])
            if nums[left] <= cur_min:
                left += 1 
            elif nums[right] >= cur_max:
                right -= 1
            else:
                break

        if left == right-1 and nums[left] <= nums[right]:
            return 0

        return right-left+1
