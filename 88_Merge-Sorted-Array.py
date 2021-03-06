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
