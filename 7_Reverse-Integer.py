# Exercise I:
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


# Exercise III:
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        res = int((str(x)[::-1])) if x >= 0 else -int(str(x)[1:][::-1])
        if res < 2**31 and res >= -2**31:
            return res

        return 0


# Exercise IV:
class Solution:
    def reverse(self, x: int) -> int:
        res = 0 
        flag = -1 if x < 0 else 1
        x = abs(x)

        while x>0:
            tmp = x%10
            res = res*10+tmp
            x = x//10
        
        if res*flag > 2**31-1 or res*flag < -2**31:
            return 0
        
        return res*flag
