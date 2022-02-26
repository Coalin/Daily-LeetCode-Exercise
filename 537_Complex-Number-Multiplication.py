class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1 = int(num1[:-1].split('+', 2)[0])
        b1 = int(num1[:-1].split('+', 2)[1])
        a2 = int(num2[:-1].split('+', 2)[0])
        b2 = int(num2[:-1].split('+', 2)[1])
        res1 = a1*a2-b1*b2 
        res2 = a1*b2+a2*b1 
        return str(res1)+'+'+str(res2)+'i'