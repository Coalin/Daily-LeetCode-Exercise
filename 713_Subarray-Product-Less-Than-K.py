class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        i = 0
        j = 0
        
        cur_mul = nums[0]
        
        while i < len(nums):
            if cur_mul < k:
                if j < len(nums)-1:
                    j += 1
                    cur_mul *= nums[j] 
                else:
                    res += j-i+1
                    i += 1
                    if i < len(nums):
                        cur_mul //= nums[j]
            else:
                res += j-i
                if i == j:
                    if i != len(nums)-1:
                        i += 1
                        j += 1
                        cur_mul = nums[j]
                    else:
                        break
                else:
                    cur_mul //= nums[i]
                    i += 1
        
        return res
        

        
        
