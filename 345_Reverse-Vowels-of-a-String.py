class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
# Method I:
        # VOWEL = ['a','e','i','o','u','A','E','I','O','U']
        # vowel = ''
        # for i in s:
        #     if i in VOWEL:
        #         vowel += i
        # count = len(vowel)-1
        # res = ''
        # for index in range(len(s)):
        #     if s[index] in VOWEL:
        #         res += vowel[count] 
        #         count -= 1
        #     else:
        #         res += s[index]
        # return res

# Method II:
        # vowel = re.findall('(?!)[aeiou]', s)
        vowel = re.findall('(?i)[aeiou]', s)
        res = re.sub("(?i)[aeiou]", lambda m: vowel.pop(), s)
        return res
    

# Exercise III:
# June 3, 2023
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = [v for v in s if v in 'aeiouAEIOU']
        ans = [vowel.pop() if v in 'aeiouAEIOU' else v for v in s ]
        return ''.join(ans)
