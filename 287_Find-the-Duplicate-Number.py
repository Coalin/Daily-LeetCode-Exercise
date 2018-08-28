class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = dict()
        for num in nums:
            if num_dict.has_key(num):
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        for i in nums:
            if num_dict[i] > 1:
                return i
