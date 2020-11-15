# Solution I: 从左到右，找第一个比后面大的字符，删除，清零，k次扫描。

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: 
            return '0'
        for _ in range(k):
            for i in range(len(num)):
                if i == len(num)-1:
                    num = num[:-1] 
                elif num[i] > num[i+1]:
                    num = num[:i]+num[i+1:]
                    break               
        return str(int(num))
        