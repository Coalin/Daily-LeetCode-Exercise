# Method I:
# Accepted while the time complexity equals to O(nlogn) due to the sort function.
# 66.68%; 144ms.

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_1 = len(nums1)
        len_2 = len(nums2)
        res = sorted(nums1+nums2)
        total_length = len_1 + len_2
        if total_length % 2 == 1:
            return res[int(total_length/2)]
        else:
            return (res[int(total_length/2-1)]+res[int(total_length/2)])/2
# Method II:
# Accepted while the time complexity equals to O(n) due to while circulation.
# 86.20%; 124ms.
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_1 = len(nums1)
        len_2 = len(nums2)
        total_length = len_1 + len_2
        res = []
        i = j = 0
        while i < len_1 and j < len_2:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
            else:
                res.extend([nums1[i], nums2[j]])
                i += 1
                j += 1
        if i == len_1:
            res.extend(nums2[j:])
        if j == len_2:
            res.extend(nums1[i:])
        if total_length % 2 == 1:
            return res[int(total_length/2)]
        else:
            return (res[int(total_length/2-1)]+res[int(total_length/2)])/2

# Method III:
# Target time complexity: O(logn)
# To be continued...

