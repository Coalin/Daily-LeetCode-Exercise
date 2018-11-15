# Method I:

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = []
        final_len = len(nums)+1
        for i in range(len(nums)):
            j = i
            cur_res = nums[i]
            while cur_res < s:
                if j == len(nums)-1:
                    break
                j += 1
                cur_res += nums[j]
            if cur_res >= s:
                cur_len = j-i+1
                final_len = min(cur_len, final_len)
        if final_len == len(nums)+1:
            return 0
        else:
            return final_len

# Method II:
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left = 1
        right = len(nums)
        while left <= right:
            mid = left + (right-left)//2
            print(left, mid, right)
            if self.window(s, nums, left) == True:
                return left
            if self.window(s, nums, right) == False:
                return 0
            if self.window(s, nums, mid) == False:
                left = mid+1
            else:
                right = mid
                        
        
    def window(self, s, nums, win_len):
        for i in range(len(nums)-win_len+1):
            cur_sum = sum(nums[i:i+win_len])
            if cur_sum >= s:
                return True
        return False
        
        
            
                    
        
