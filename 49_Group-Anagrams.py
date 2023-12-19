# Exercise I:
# Dec 19, 2023

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = dict()

        for word in strs:
            word_sorted = ''.join(sorted(word))
            if word_sorted in res_dict:
                res_dict[word_sorted].append(word)
            else:
                res_dict[word_sorted] = [word]

        return list(res_dict.values())
