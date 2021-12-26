class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        text_word = text.split(' ')

        for i in range(len(text_word)-2):
            if text_word[i] == first and text_word[i+1] == second:
                res.append(text_word[i+2])
        return res
