# Exercise I:
# Apr 18, 2023

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0 
        right = len(nums)-1
        cnt = 0

        while left < right:
            if nums[left]+nums[right] < k:
                left += 1
            elif nums[left]+nums[right] > k:
                right -= 1
            else:
                left += 1
                right -= 1
                cnt += 1

        return cnt
