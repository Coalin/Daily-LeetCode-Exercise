class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur_len = 0
        total_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cur_len = 0
            else:
                cur_len += 1
            total_len = max(total_len, cur_len)
        return total_len
            
        
