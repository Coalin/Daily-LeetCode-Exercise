class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_dict = {}
        res = []
        for num in nums:
            if num_dict.has_key(num):
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        for i in num_dict:
            if num_dict[i] > len(nums)/3:
                res.append(i)
        return res

            
        
