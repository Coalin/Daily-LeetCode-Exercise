class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = ''
        length = 0
        if len(s) == 0:
            return 0
        for i in reversed(s):
            if i == ' ' and str != '':
                return length
            if i != ' ':
                length += 1
                str += i 
        return length
        
   # 注意会有形如“a "的测试用例。


# Exercise II:
# Dec 15, 2023
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
