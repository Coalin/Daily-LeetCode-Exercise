class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        num_dict = {}
        for item in nums:
            if item in num_dict:
                num_dict[item] += 1
            else:
                num_dict[item] = 1
        for i in num_dict:
            if num_dict[i] >= 2:
                return True
        return False


# Exercise II:
# Jan 9, 2023
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res_dic = {}

        for i in range(len(nums)):
            if nums[i] in res_dic:
                return True 
            else:
                res_dic[nums[i]] = 1

        return False
