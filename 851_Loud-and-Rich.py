class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        N = len(quiet)

        self.richer = dict()
        res_dic = dict()
        
        for rich in richer:
            if rich[1] in self.richer:
                self.richer[rich[1]].append(rich[0])
            else:
                self.richer[rich[1]] = [rich[0]]
        
        for key in self.richer:
            stack = self.richer[key][:]
            while stack:
                node = stack.pop()
                if node in self.richer:
                    # for j in self.richer[node]:
                    #     if j not in self.richer[key]:
                    #         self.richer[key].append(j)
                    #         stack.append(j)
                    self.richer[key] = list(set(self.richer[key]+self.richer[node]))
                    stack = list(set(stack+self.richer[node]))
                            
        for i in range(N):
            res_dic[i] = i

        for key in self.richer:
            cur_min = quiet[key]
            for i in self.richer[key]:
                if quiet[i] < cur_min:
                    cur_min = quiet[i]
                    res_dic[key] = i
        
        res = []
        for i in range(N):
            res.append(res_dic[i])
        
        return res
                
                
        
        
            
            
            
        
            
        
            
            
            
        
        
