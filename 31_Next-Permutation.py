class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
# Attempt I: Failed

        # if len(nums) > 1:
        #     num_dict = dict()
        #     for i in reversed(range(len(nums))):
        #         for j in reversed(range(i)):
        #             if nums[j] < nums[i]:
        #                 num_dict[i] = j
        #                 break
        #     left = -1
        #     for index in num_dict:
        #         left = max(num_dict[index], left)
        #     right = 0
        #     for index_ in num_dict:
        #         if num_dict[index_] == left:
        #             right = index_
        #     if right:
        #         middle = nums[right]
        #         for i in reversed(range(left, right)):
        #             nums[i+1] = nums[i]
        #         nums[left] = middle
        
# Attempt II: Accepted:
# Reference: https://blog.csdn.net/zr1076311296/article/details/51296008

        if len(nums) > 1:
            pos = -1
            for i in reversed(range(len(nums))):
                if nums[i-1] < nums[i]:
                    pos = i
                    break
            if pos != -1:
                for j in reversed(range(len(nums))):
                    if nums[j] > nums[pos-1]:
                        nums[pos-1], nums[j] = nums[j], nums[pos-1]
                        break
                nums[pos:] = sorted(nums[pos:])
            else:
                nums.sort()
        
