class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = dict()
        for num in nums:
            if dic.has_key(num):
                dic[num] += 1
            else:
                dic[num] = 1
        result = []
        for key in dic:
            if dic[key] == 1:
                result.append(key)
        return result
