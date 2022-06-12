class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            if self.is_same_pattern(word, pattern):
                res.append(word)
        return res

    def is_same_pattern(self, word, pattern):
        if len(word) != len(pattern):
            return 0 
        my_dic = dict()
        for i in range(len(word)):
            if pattern[i] not in my_dic:
                my_dic[pattern[i]] = word[i]
            else:
                if my_dic[pattern[i]] != word[i]:
                    return 0 
        res_lst = [my_dic[k] for k in my_dic]
        res_set = set([my_dic[k] for k in my_dic])
        if len(res_lst) != len(res_set):
            return 0
        return 1
