# Exercise I:
# Mar 18, 2024
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_dict = {'2': 'abc', 
                      '3': 'def',
                      '4': 'ghi',
                      '5': 'jkl',
                      '6': 'mno',
                      '7': 'pqrs',
                      '8': 'tuv',
                      '9': 'wxyz' 
        }

        res = []

        # 当前的组合 combination 
        # 剩余的数字字符串 next_digits
        def backtrack(combination, next_digits):
            if len(combination) == len(digits):
                res.append(combination)
                return 

            digit = next_digits[0]
            letters = digit_dict[digit]
            for letter in letters:
                backtrack(combination+letter, next_digits[1:])

        backtrack('', digits)

        return res
