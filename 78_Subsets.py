# Method I

import copy

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        res = [[], [nums[0]]]
        if len(nums) == 1:
            return res
        for i in range(1, len(nums)):
            res_backup = copy.deepcopy(res)
            for item in res:
                item.append(nums[i])
            res += res_backup
        return res
 
# 85.66%; 52ms.
# 注意：list的复制，用copy.deepcopy().
# https://blog.csdn.net/u010712012/article/details/79754132
