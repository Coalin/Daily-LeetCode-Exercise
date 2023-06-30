# Exercise I
# July 1, 2023

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 1
        j = 1 
        cur_char = chars[0]
        cur_char_cnt = 1

        while i < len(chars) and j < len(chars):
            if chars[i] == cur_char:
                cur_char_cnt += 1
            else:
                if cur_char_cnt != 1:
                    if cur_char_cnt <= 9:
                        chars[j] = str(cur_char_cnt)
                        j += 1
                    else:
                        chars[j] = str(cur_char_cnt//10)
                        j += 1
                        chars[j] = str(cur_char_cnt%10)
                        j += 1
                cur_char = chars[i]
                chars[j] = cur_char
                j += 1
                cur_char_cnt = 1
            i += 1

        if j < len(chars):
            if cur_char_cnt <= 9:
                chars[j] = str(cur_char_cnt)
            elif cur_char_cnt <= 99:
                chars[j] = str(cur_char_cnt//10)
                j += 1
                chars[j] = str(cur_char_cnt%10)
            elif cur_char_cnt <= 999:
                chars[j] = str(cur_char_cnt//100)
                j += 1
                chars[j] = str((cur_char_cnt%100)//10)
                j += 1
                chars[j] = str(cur_char_cnt%10)
            else:
                chars[j] = str(cur_char_cnt//1000)
                j += 1
                chars[j] = str((cur_char_cnt%1000)//100)
                j += 1
                chars[j] = str((cur_char_cnt%100)//10)
                j += 1
                chars[j] = str(cur_char_cnt%10)

        if cur_char_cnt == 1:
            return j
        else:
            return j+1
