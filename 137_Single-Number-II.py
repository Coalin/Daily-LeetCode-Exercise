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
