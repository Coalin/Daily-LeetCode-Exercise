class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for num in nums:
            if dic.has_key(num):
                dic[num] += 1
            else:
                dic[num] = 1
        for key in dic:
            if dic[key] == 1:
                return key
            
# Exercise II:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums))*2-sum(nums)


# Exercise III:
# Mar 2, 2023
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 

        for num in nums:
            res = num^res 

        return res
