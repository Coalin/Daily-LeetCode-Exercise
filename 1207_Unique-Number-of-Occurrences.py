# Exercise I:
# May 21, 2023

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        freq_cnt = {}
        for key in freq:
            if freq[key] in freq_cnt:
                return False
            else:
                freq_cnt[freq[key]] = 1

        return True     
            