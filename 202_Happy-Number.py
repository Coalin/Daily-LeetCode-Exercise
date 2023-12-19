class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_dict = dict()
        while True:
            num_dict[n] = True
            num_sum = 0
            while n > 0:
                num_sum += (n%10)*(n%10) 
                n /= 10
            if num_sum == 1:
                return True
            elif num_sum in num_dict:
                return False
            else:
                n = num_sum
        

# Exercise II:
# Dec 19, 2023
class Solution:
    def isHappy(self, n: int) -> bool:
    
        def one_step(s):
            i = 0 
            res = 0

            while i < len(s):
                res += int(s[i])*int(s[i])
                i += 1

            return str(res) 

        s_s = str(n)
        s_list = []

        while True:
            s_s = one_step(s_s)
            if s_s == '1':
                return True 
            if s_s in s_list:
                return False
            s_list.append(s_s)

        return False
