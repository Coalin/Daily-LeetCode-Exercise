class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s 

        res = [['0'] for _ in range(numRows+1)]
        for i in range(len(s)):
            if i % (2*numRows-2) <= numRows-1:
                res[i % (2*numRows-2)].append(s[i])
            else:
                res[numRows-(i % (2*numRows-2))%numRows-2].append(s[i])

        final_res = ''
        for idx in range(len(res)):
            final_res +=  "".join(res[idx][1:]) 
        
        return final_res