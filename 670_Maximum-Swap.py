class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num)) == 1:
            return num
        p = 0
        
        while p < len(str(num))-1:
            cur_list = list(str(num))
            cur_max = self.curMax(int(str(num)[p+1:]))
                
            if str(num)[p:][0] == '0':
                for i in reversed(range(p+1, len(str(num)))):
                    if int(str(num)[i]) == cur_max:
                        mid = cur_list[p]
                        cur_list[p] = cur_list[i]
                        cur_list[i] = mid
                        return int(''.join(cur_list))
                    
            if self.isMax(int(str(num)[p:])):
                p += 1
                
            else:
                for i in reversed(range(p+1, len(str(num)))):
                    if int(str(num)[i]) == cur_max:
                        mid = cur_list[p]
                        cur_list[p] = cur_list[i]
                        cur_list[i] = mid
                        return int(''.join(cur_list))
        return num
                
    def isMax(self, num):
        return int(str(num)[0]) == max([int(x) for x in list(str(num))])
    
    def curMax(self, num):
        return max([int(x) for x in list(str(num))])
        
