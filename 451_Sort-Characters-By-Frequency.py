class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_dic = {}
        res = ''
        
        for i in range(len(s)):
            if s[i] in num_dic:
                num_dic[s[i]] += 1
            else:
                num_dic[s[i]] = 1
        
        letter = self.sort_by_value(num_dic)
        
        while letter:
            node = letter.pop()
            for _ in range(num_dic[node]):
                res += node
        return res
    
    def sort_by_value(self, d):
        items=d.items()
        backitems=[[v[1],v[0]] for v in items]
        backitems.sort()
        return [backitems[i][1] for i in range(len(backitems))]
                
