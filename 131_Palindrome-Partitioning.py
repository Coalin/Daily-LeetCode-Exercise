class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        ans = []

        def is_palindrome(i, j):
            if i >= j:
                return 1
            if s[i] == s[j]:
                return is_palindrome(i+1, j-1)
            else:
                return 0

        def dfs(start):
            if start == len(s):
                # print(ans)
                res.append(ans[:])
                # print(res)
                return 

            for end in range(start, len(s)):
                # print(start, end, is_palindrome(start, end))
                if is_palindrome(start, end):
                    ans.append(s[start:end+1])
                    dfs(end+1)
                    ans.pop()

        dfs(0)
        return res
