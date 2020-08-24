class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)//2+1):
            if len(s)%i == 0:
                cur_str = s[:i]
                lon_str = '' 
                for _ in range(len(s)//i):
                    lon_str += cur_str
                if lon_str == s:
                    return True 
        
        return False 