# Exercise I:
# July 8, 2023

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1 
        r = n 
        while l <= n:
            m = (r-l)//2+l
            if guess(l) == 0:
                return l 
            if guess(r) == 0:
                return r 
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                r = m 
            elif guess(m) == 1:
                l = m 
            else:
                return 
        
        return
