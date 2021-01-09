class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        s = s+'0'
        res = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] != s[i]:
                    if j >= i+3:
                        flag = 0
                        if res:
                            for inter in res:
                                if i <= inter[1]:
                                    flag = 1
                            if not flag:
                                res.append([i, j-1])
                        else:
                            res.append([i,j-1])
                    break
        return res
              