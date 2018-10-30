# Method I: Linear
# Complexity: O(n)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = -10000000000
        cursum = -10000000000
        for num in nums:
            cursum = max(num, cursum+num)
            maxsum = max(cursum, maxsum)
        return maxsum

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        cur_res = nums[0]
        final_res = nums[0]
        for i in range(1, len(nums)):
            cur_res = max(cur_res+nums[i], nums[i])
            final_res = max(cur_res, final_res)
        return final_res
    
# Method II: DP
# Complexity: O(n)

class Solution(object):
   def maxSubArray(self, nums):
       """
       :type nums: List[int]
       :rtype: int
       """
       dp = [-10086 for _ in range(len(nums))]
       dp[0] = nums[0]
       for i in range(1, len(nums)):
           dp[i] = max(dp[i-1]+nums[i], nums[i])
       return max(dp)

# Method III: Divide and Conquer
# Complexity: O(nlogn)
# "Introduction to Algorithms: P66"
# 4.96%; 116ms.

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp = [nums[0] for col in range(len(nums))]
        # for i in range(1, len(nums)):
        #     dp[i] = max(dp[i-1]+nums[i], nums[i])
        # return max(dp)
        import sys
        sys.setrecursionlimit(10000000)
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        low = 0
        high = len(nums)-1
        sum_ = self.maxSubArray_(nums, low, high)
        return sum_
        
        
    def maxSubArray_(self, nums, low, high):
        if low == high:
            return nums[low]
        else:
            mid = (low+high)//2
            left_sum = self.maxSubArray_(nums, low, mid)
            right_sum = self.maxSubArray_(nums, mid+1, high)
            cross_sum = self.maxCrossingSubArray(nums, low, mid, high)
            if left_sum >= cross_sum and left_sum >= right_sum:
                return left_sum
            elif right_sum >= cross_sum and right_sum >= left_sum:
                return right_sum
            else:
                return cross_sum
            
    
    def maxCrossingSubArray(self, nums, low, mid, high):
        if low == mid:
            if nums[low] > 0 and nums[high] > 0:
                return nums[low]+nums[high]
            else:
                return max(nums[low], nums[high])
        left_sum = nums[mid]
        right_sum = nums[mid+1]
        cur_sum_left = nums[mid]
        cur_sum_right = nums[mid+1]

        for i in reversed(range(low, mid)):
            cur_sum_left += nums[i]
            if cur_sum_left > left_sum:
                left_sum = cur_sum_left

        for j in range(mid+2, high + 1):
            cur_sum_right += nums[j]
            if cur_sum_right > right_sum:
                right_sum = cur_sum_right

        sum_all = left_sum + right_sum
        return sum_all
                          
                          
                
        
