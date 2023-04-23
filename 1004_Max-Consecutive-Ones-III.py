class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left_before_sum = 0 
        right_before_sum = 1 if nums[0] == 0 else 0 
        left = 0
        res = 0

        if len(nums) == 1:
            if nums == [0] and k == 1 or nums == [1]:
                return 1
            else:
                return 0

        for right in range(1, len(nums)):
            right_before_sum += 1-nums[right]
            while right_before_sum-left_before_sum > k:
                left_before_sum += 1-nums[left]
                left += 1
            res = max(res, right-left+1)

        return res
