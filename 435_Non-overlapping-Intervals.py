# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda Interval: Interval.start)
        count = 0
        pre = intervals[0]
        
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if pre.end > cur.start:
                if pre.end >= cur.end:
                    pre = cur
                count += 1    
            else:
                pre = cur
        
        return count
                    
                
        
