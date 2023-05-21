# Exercise I:
# May 21, 2023

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[], []]
        nums_1 = set(nums1)
        nums_2 = set(nums2)

        for i in nums_1:
            if i not in nums_2:
                res[0].append(i)

        for j in nums_2:
            if j not in nums_1:
                res[1].append(j)

        return res
