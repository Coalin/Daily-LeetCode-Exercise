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
    
