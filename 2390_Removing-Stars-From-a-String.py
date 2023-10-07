# Exercise I
# Oct 7, 2023

class Solution:
    def removeStars(self, s: str) -> str:
        my_stack = []
        for i in s:
            if i == '*':
                if my_stack:
                    my_stack.pop()
            else:
                my_stack.append(i)
        
        res = ''
        for j in my_stack:
            res += j 

        return res
