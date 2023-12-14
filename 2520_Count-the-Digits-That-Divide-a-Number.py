# Exercise I:
# Oct 26, 2023
class Solution:
    def countDigits(self, num: int) -> int:
        res = []
        for i in range(len(str(num))):
            cur_num = int(str(num)[i])
            if cur_num != 0:
                if num % cur_num == 0:
                    res.append(cur_num)
        return len(res)
