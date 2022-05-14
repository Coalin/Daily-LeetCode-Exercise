# Solution I: O(n^2), Time out
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         res = 0

#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if sum(nums[i:j+1]) == k:
#                     res += 1

#         return res


# Solution II: O(n), Hash Table 
# 前缀和 哈希表
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pre_sum = 0
        res_hash = {0:1}

        for i in range(len(nums)):
            pre_sum += nums[i]
            if pre_sum-k in res_hash:
                res += res_hash[pre_sum-k]
            if pre_sum in res_hash:
                res_hash[pre_sum] += 1
            else:
                res_hash[pre_sum] = 1 
        return res
