class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sort = sorted(nums)
        left = 0
        right = len(nums_sort)-1
        while left < right:
            if nums_sort[left] + nums_sort[right] == target:
                break
            if nums_sort[left] + nums_sort[right] < target:
                left += 1
            if nums_sort[left] + nums_sort[right] > target:
                right -= 1
        for i in range(len(nums)):
            if nums[i] == nums_sort[left]:
                l = i
        for j in range(len(nums)):
            if nums[j] == nums_sort[right] and j != l:
                r = j
        return [l, r]
