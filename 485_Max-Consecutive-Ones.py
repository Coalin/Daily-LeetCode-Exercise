# Exercise I:
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
            
     
# Exercise II:
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = 0
        cur_res = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(cur_res, res)
                cur_res = 0
            else:
                cur_res += 1
            
        res = max(cur_res, res)
                
        return res
    
 
# Exercise III:
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([len(i) for i in "".join([str(i) for i in nums]).split("0")])
