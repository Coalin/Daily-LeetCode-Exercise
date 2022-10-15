# Exercise I:
# 65.95%; 820 ms
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = right = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-2 > right-left:
                left = l+1
                right = r-1
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-2 > right-left:
                left = l+1
                right = r-1
        return s[left:right+1]
        

# Exercise II:
# Feb 20, 2019
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = 1
        L = R = 0
        
        for i in range(len(s)-1):
            left = right = i
            while left > 0 and right < len(s)-1:
                if s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                else:
                    break
            cur_len = right-left+1
            if cur_len > res:
                L = left
                R = right
                res = cur_len
            
            if (len(s)-i-1)*2 > res:
                start = i
                end = i+1
                cur_len_ = 1
                if s[start] == s[end]:
                    while start > 0 and end < len(s)-1:
                        if s[start-1] == s[end+1]:
                            start -= 1
                            end += 1
                        else:
                            break
                    cur_len_ = end-start+1
                    if cur_len_ > res:
                        L = start
                        R = end
                        res = cur_len_
                        
        return s[L:R+1]
                

# Exercise III:
# Oct 15, 2022
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = right = 0

        for i in range(len(s)):
            l = r = i 
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-2 > right-left:
                left = l+1 
                right = r-1
            
            l = i 
            r = i+1 
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l -= 1 
                r += 1 
            if r-l-2 > right-left:
                left = l+1 
                right = r-1

        return s[left:right+1]            
