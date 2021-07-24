class Solution:
    def maximumTime(self, time: str) -> str:
        hour = time.split(':')[0]
        minite = time.split(':')[1]
        if hour[0] == '?':
            if hour[1] == '?':
                res_hour = '23'
            elif hour[1] <= '3':
                res_hour = str(2)+str(hour[1])
            else:
                res_hour = str(1)+str(hour[1])
        else:
            if hour[1] == '?':
                if hour[0] <= '1':
                    res_hour = str(hour[0])+str(9)
                else:
                    res_hour = str(hour[0])+str(3)
            else:
                res_hour = hour 
        
        if minite[0] == '?':
            if minite[1] == '?':
                res_minite = '59'
            else:
                res_minite = str(5)+str(minite[1])
        else:
            if minite[1] == '?':
                res_minite = str(minite[0])+str(9)
            else:
                res_minite = minite 

        return res_hour+':'+res_minite
