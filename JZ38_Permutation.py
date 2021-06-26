class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []
        used = [0 for _ in range(len(s))]
        def backtrack(nums, used, path):
            if len(path) == len(nums):
                mid = ''
                for char in path:
                    mid += char 
                res.append(mid)
                return 
            for i in range(len(nums)):
                if used[i] == 0:
                    if i > 0 and nums[i] == nums[i-1] and used[i-1] == 1:
                        continue 
                    used[i] = 1
                    path.append(nums[i])
                    backtrack(nums, used, path)
                    path.pop()
                    used[i] = 0
        backtrack(sorted(s), used, [])
        return res