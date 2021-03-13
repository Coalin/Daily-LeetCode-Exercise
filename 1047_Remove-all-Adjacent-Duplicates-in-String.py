class Solution:
    def removeDuplicates(self, S: str) -> str:
        res_stack = [S[0]]

        if len(S) >= 2:
            for i in range(1, len(S)):
                if len(res_stack) > 0:
                    if S[i] == res_stack[-1]:
                        res_stack.pop()
                    else:
                        res_stack.append(S[i])
                else:
                    res_stack.append(S[i])                

        res_str = ''
        for j in res_stack:
            res_str += j 
        return res_str
        