class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [0 for _ in range(len(s))]
        
        left = 0
        while left <= len(s)-1:
            if s[:left+1] in wordDict:
                dp[left] = 1
            left += 1
            
        for i in range(1, len(s)):
            for j in range(i):
                if dp[j] and s[j+1:i+1] in wordDict:
                    dp[i] = 1
                    break

        return True if dp[-1] == 1 else False
            
        
