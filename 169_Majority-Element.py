class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = dict()
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if temp.has_key(num):
                temp[num] += 1
                if temp[num] > len(nums)/2:
                    return num
            else:
                temp[num] = 1
