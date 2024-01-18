# Exercise I:
# Jan 18, 2024
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_sum_max = nums[0]
        res_sum_max = nums[0]
        cur_sum_min = nums[0]
        res_sum_min = nums[0]

        for i in range(1, len(nums)):
            cur_sum_max = max(cur_sum_max+nums[i], nums[i])
            res_sum_max = max(cur_sum_max, res_sum_max)

        for j in range(1, len(nums)):
            cur_sum_min = min(cur_sum_min+nums[j], nums[j])
            res_sum_min = min(cur_sum_min, res_sum_min)
        
        if sum(nums) == res_sum_min:
            return res_sum_max

        return max(res_sum_max, sum(nums)-res_sum_min)
