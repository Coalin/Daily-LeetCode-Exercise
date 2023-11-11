# Method I:

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(len(nums2)):
            nums1[m+i] = nums2[i]
        nums1.sort()
        
        """
        The above solution runs for 40ms and can be simplified as 
        nums1[m:] = nums2[:n]
        nums1.sort()
        """
        
# Method II:

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        k = m+n
        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[k-1] = nums1[m-1]
                m -= 1
            else:
                nums1[k-1] = nums2[n-1]
                n -= 1
            k -= 1
        if n:
            nums1[:n] = nums2[:n]
            
# 90.22%; 48ms.


# Exercise III:
# Feb 1, 2023
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind_1 = m-1
        ind_2 = n-1
        idx = m+n-1
        
        while ind_1 >= 0 and ind_2 >= 0:
            if nums1[ind_1] < nums2[ind_2]:
                nums1[idx] = nums2[ind_2] 
                ind_2 -= 1
            else:
                nums1[idx] = nums1[ind_1]
                ind_1 -= 1
            idx -= 1

        if ind_1 < 0:
            while ind_2 >= 0:
                nums1[idx] = nums2[ind_2] 
                ind_2 -= 1
                idx -= 1


# Exercise IV:
# Nov 11, 2023
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind_1 = m-1 
        ind_2 = n-1 
        idx = m+n-1
        while ind_1 >= 0 and ind_2 >= 0:
            if nums1[ind_1] <= nums2[ind_2]:
                nums1[idx] = nums2[ind_2]
                ind_2 -= 1
            else:
                nums1[idx] = nums1[ind_1]
                ind_1 -= 1 
            idx -= 1
        
        if ind_1 < 0:
            while ind_2 >= 0:
                nums1[idx] = nums2[ind_2]
                ind_2 -= 1
                idx -= 1
