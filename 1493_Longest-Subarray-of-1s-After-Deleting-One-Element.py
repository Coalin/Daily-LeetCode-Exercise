class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0 
        zero_cnt = 1 if nums[0] == 0 else 0
        cur_len = 0
        max_len = 0 

        for i in range(1, len(nums)):
            zero_cnt = zero_cnt+1 if nums[i] == 0 else zero_cnt
            while zero_cnt > 1:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            max_len = max(max_len, i-left)

        return max_len
