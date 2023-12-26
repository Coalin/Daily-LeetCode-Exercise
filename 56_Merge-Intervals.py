# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        for i in sorted(intervals, key=lambda x: x.start):
            if ans and ans[-1].end >= i.start:
                ans[-1].end = max(ans[-1].end, i.end)                
            else:
                ans.append(i)
        return ans


# Exercise II:
# Dec 25, 2023
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key=lambda x:x[0])

        i = 0
        while i < len(intervals):
            left = intervals[i][0]
            right = intervals[i][1]
            while i+1 < len(intervals) and intervals[i+1][0] <= right:
                i += 1
                right = max(right, intervals[i][1])
            res.append([left, right])
            i += 1

        return res
