class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return matrix
        
        m = len(matrix)
        n = len(matrix[0])
        
        pacific = [[0 for col in range(n)] for row in range(m)]
        atlantic = [[0 for col in range(n)] for row in range(m)]
        paci_stack = []
        atlan_stack = []
        res = []
        
        for i in range(n):
            pacific[0][i] = 1
            atlantic[m-1][i] = 1
            paci_stack.append([0, i])
            atlan_stack.append([m-1,i])
            
        for j in range(m):
            pacific[j][0] = 1
            atlantic[j][n-1] = 1
            paci_stack.append([j, 0])
            atlan_stack.append([j, n-1])
    
        while paci_stack:
            node = paci_stack.pop()
            if node[1]-1 >= 0:
                left_ = [node[0], node[1]-1]
                if matrix[node[0]][node[1]-1] >= matrix[node[0]][node[1]] and pacific[node[0]][node[1]-1] == 0:
                    pacific[node[0]][node[1]-1] = 1
                    paci_stack.append(left_)
            if node[1]+1 <= n-1:
                right_ = [node[0], node[1]+1]
                if matrix[node[0]][node[1]+1] >= matrix[node[0]][node[1]] and pacific[node[0]][node[1]+1] == 0:
                    pacific[node[0]][node[1]+1] = 1 
                    paci_stack.append(right_)
            if node[0]-1 >= 0:
                up_ = [node[0]-1, node[1]]
                if matrix[node[0]-1][node[1]] >= matrix[node[0]][node[1]] and pacific[node[0]-1][node[1]] == 0:
                    pacific[node[0]-1][node[1]] = 1
                    paci_stack.append(up_)
            if node[0]+1 <= m-1:
                down_ = [node[0]+1, node[1]]
                if matrix[node[0]+1][node[1]] >= matrix[node[0]][node[1]] and pacific[node[0]+1][node[1]] == 0:
                    pacific[node[0]+1][node[1]] = 1 
                    paci_stack.append(down_)

                    
        while atlan_stack:
            node = atlan_stack.pop()
            if node[1]-1 >= 0:
                left_ = [node[0], node[1]-1]
                if matrix[node[0]][node[1]-1] >= matrix[node[0]][node[1]] and atlantic[node[0]][node[1]-1] == 0:
                    atlantic[node[0]][node[1]-1] = 1
                    atlan_stack.append(left_)
            if node[1]+1 <= n-1:
                right_ = [node[0], node[1]+1]
                if matrix[node[0]][node[1]+1] >= matrix[node[0]][node[1]] and atlantic[node[0]][node[1]+1] == 0:
                    atlantic[node[0]][node[1]+1] = 1
                    atlan_stack.append(right_)
            if node[0]-1 >= 0:
                up_ = [node[0]-1, node[1]]
                if matrix[node[0]-1][node[1]] >= matrix[node[0]][node[1]] and atlantic[node[0]-1][node[1]] == 0:
                    atlantic[node[0]-1][node[1]] = 1
                    atlan_stack.append(up_)
            if node[0]+1 <= m-1:
                down_ = [node[0]+1, node[1]]
                if matrix[node[0]+1][node[1]] >= matrix[node[0]][node[1]] and atlantic[node[0]+1][node[1]] == 0:
                    atlantic[node[0]+1][node[1]] = 1
                    atlan_stack.append(down_)
            
        for i in range(m):
            for j in range(n):
                if pacific[i][j]*atlantic[i][j] == 1:
                    res.append([i, j])
        return res
        
        
            
        
        
        
