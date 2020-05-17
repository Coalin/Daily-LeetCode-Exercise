class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(i, adj_matrix, flag):
            if adj_matrix[i] == []:
                return True
            if flag[i] == -1:
                return True
            if flag[i] == 1:
                return False
            flag[i] = 1
            for j in adj_matrix[i]:
                if not dfs(j, adj_matrix, flag):
                    return False
            flag[i] = -1
            return True 
        
        flag = [0 for _ in range(numCourses)]
        adj_matrix = [[] for _ in range(numCourses)]
        for pre, cur in prerequisites:
            adj_matrix[pre].append(cur) 
        for i in range(numCourses):
            if not dfs(i, adj_matrix, flag):
                return False
        return True
