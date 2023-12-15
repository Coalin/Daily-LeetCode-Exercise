# Exercise I:
# Dec 15, 2023

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_cnt = len(words)
        words_len = len(words[0])
        window_len = words_cnt*words_len
        s_len = len(s)
        res = []

        words_freq = dict()
        for word in words:
            if word in words_freq:
                words_freq[word] += 1
            else:
                words_freq[word] = 1 

        for i in range(s_len-window_len+1):
            cur_str = s[i:i+window_len]
            cur_freq = dict()
            for j in range(words_cnt):
                if cur_str[j*words_len:(j+1)*words_len] in cur_freq:
                    cur_freq[cur_str[j*words_len:(j+1)*words_len]] += 1
                else:
                    cur_freq[cur_str[j*words_len:(j+1)*words_len]] = 1
            if cur_freq == words_freq:
                res.append(i) 

        return res
