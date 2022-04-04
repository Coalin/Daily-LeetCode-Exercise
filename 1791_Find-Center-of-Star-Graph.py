class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        my_dic = dict()
        for edge in edges:
            if edge[0] in my_dic:
                my_dic[edge[0]] += 1
            else:
                my_dic[edge[0]] = 1 
            if edge[1] in my_dic:
                my_dic[edge[1]] += 1
            else:
                my_dic[edge[1]] = 1
        for key in my_dic:
            if my_dic[key] != 1:
                return key            