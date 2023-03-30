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


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for index, num in enumerate(nums):
            if target-num in num_dict:
                return [index, num_dict[target-num]]
            num_dict[num] = index


# Exercise II:
# Mar 30, 2023
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()

        for i in range(len(nums)):
            if target-nums[i] in my_dict:
                return [i, my_dict[target-nums[i]]]
            my_dict[nums[i]] = i 
