class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        res = ''
        break_point = 0
        if x < 0:
            x = -x
            flag = 1
        reversed_list = []
        x = str(x)
        for i in reversed(range(len(x))):
            reversed_list.append(x[i])
        for i in range(len(reversed_list)):
            if reversed_list[i] != '0':
                break_point = i
                break
        for item in reversed_list[break_point:]:
            res += item
        if flag == 0:
            if int(res) <= 2**31-1:
                return int(res)
            else:
                return 0
        else:
            if int(res) < 2**31:
                return -int(res)
            else:
                return 0
    
    
# Exercise II:
class Solution:
    def reverse(self, x: 'int') -> 'int':
        res = int(str(abs(x))[::-1])
        if res > 2**31-1:
            return 0
        if x < 0:
            return res*(-1)
        elif x == 0:
            return 0
        else:
            return res
        
