# Exercise I:
# Dec 23, 2023

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        final_len = 1

        for num in nums:
            if num-1 not in nums_set:
                cur_num = num 
                cur_len = 1
                while cur_num+1 in nums_set:
                    cur_len += 1
                    cur_num += 1
                final_len = max(final_len, cur_len)

        return final_len
