class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        alpha = {}
        for letter in s:
            if letter not in alpha:
                alpha[letter] = 1
            else:
                alpha[letter] += 1
        
        key_val = []
        for i in range(len(s)):
            # 如果它已经存在于栈中，则不能加入字符 s[i]
            if s[i] not in key_val:
                # 如果栈顶字符大于当前字符 s[i]，说明栈顶字符为「关键字符」，故应当被去除
                while key_val:
                    if key_val[-1] > s[i] and alpha[key_val[-1]] > 0:
                        # 在弹出栈顶字符时，如果字符串在后面的位置上再也没有这一字符，则不能弹出栈顶字符。
                        key_val.pop()
                    else:
                        break
                key_val.append(s[i])
            alpha[s[i]] -= 1

        res = ''
        for char in key_val:
            res += char

        return res
            