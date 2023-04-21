class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cur_v = 0 
        for i in range(k):
            if s[i] in ('a', 'e', 'i', 'o', 'u'):
                cur_v += 1
        max_v = cur_v 

        for j in range(1, len(s)-k+1):
            if s[j+k-1] in ('a', 'e', 'i', 'o', 'u'):
                cur_v += 1
            if s[j-1] in ('a', 'e', 'i', 'o', 'u'):
                cur_v -= 1
            max_v = max(max_v, cur_v)

        return max_v
