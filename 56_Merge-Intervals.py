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
