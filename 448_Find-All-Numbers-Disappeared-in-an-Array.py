class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_ = len(nums)
        nums = list(set(nums))
        num_dic = {}
        res = []
        
        for i in nums:
            num_dic[i] = 1
        for i in range(1, len_+1):
            if i not in num_dic:
                res.append(i)
        return res
        
        
