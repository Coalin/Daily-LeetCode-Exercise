class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1


# Exercise II:
# Dec 14, 2023
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers)-1

        while left < right:
            if numbers[left]+numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left]+numbers[right] < target:
                left += 1
            else:
                right -= 1
