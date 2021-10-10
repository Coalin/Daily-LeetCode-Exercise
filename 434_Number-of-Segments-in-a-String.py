class Solution:
    def countSegments(self, s: str) -> int:
        lst = s.split(' ')
        res = 0
        for i in lst:
            if i != '':
                res += 1 
        return res
