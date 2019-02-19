class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.sub(s, k, 0, len(s)-1)
        
    def sub(self, s, k, left, right):
        print([left, right])
        if left > right:
            return 0
        
        # if left == right:
        #     if k == 1:
        #         return 1
        #     else:
        #         return 0
        
        if right-left+1 < k:
            return 0
        
        count_dic = dict()
        for item in s[left:right+1]:
            if item in count_dic:
                count_dic[item] += 1
            else:
                count_dic[item] = 1
        
        neg_word = []
        for word in count_dic:
            if count_dic[word] < k:
                neg_word.append(word)
        
        if len(neg_word) == len(set(s[left:right+1])):
            return 0
        
        if neg_word:
            for neg in neg_word:
                pos = s[left:right+1].index(neg)+left
                if pos != left and pos != right:
                    return max(self.sub(s, k, left, pos-1), self.sub(s, k, pos+1, right))
                elif pos == left:
                    return self.sub(s, k, left+1, right)
                elif pos == right:
                    return self.sub(s, k, left, right-1)
        
        return right-left+1
        
        
                
            
            
            
        
