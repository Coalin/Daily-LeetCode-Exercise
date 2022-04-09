class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.palindromic(s, i, i)
            res += self.palindromic(s, i, i+1)
        return res

    def palindromic(self, s, left, right):
        num = 0 
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1 
            right += 1 
            num += 1
        return num
