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
        
