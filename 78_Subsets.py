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


# Method II:
class Solution:
    def dfs(self, res, nums, cur, index):
        if index >= len(nums):
            res.append(cur.copy())
            return 

        cur.append(nums[index])
        self.dfs(res, nums, cur, index+1)

        cur.pop()
        self.dfs(res, nums, cur, index+1)

    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(res, nums, cur = [], index = 0)
        return res 


# Exercise III:
# Feb 4, 2023
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in range(len(nums)):
            cur = []
            for item in res:
                item_copy = copy.deepcopy(item)
                item_copy.append(nums[i])
                cur.append(item_copy)
            res.extend(cur) 

        return res
