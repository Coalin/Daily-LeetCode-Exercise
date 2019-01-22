class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if duration == 0 or not timeSeries:
            return 0
        
        series_ = [[timeSeries[0], timeSeries[0]+duration-1]]
        for i in range(1, len(timeSeries)):
            if timeSeries[i] > series_[-1][1]:
                series_.append([timeSeries[i], timeSeries[i]+duration-1])
            else:
                if timeSeries[i]+duration-1 > series_[-1][1]:
                    series_[-1][1] = timeSeries[i]+duration-1
        
        res = 0
        for j in range(len(series_)):
            res += (series_[j][1]-series_[j][0]+1)
            
        return res

                
        
