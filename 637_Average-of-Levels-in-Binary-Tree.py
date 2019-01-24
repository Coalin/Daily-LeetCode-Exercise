# Method I:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        res = []
        final_res = []
        q = deque()
        q.append([root, 0])
        
        while q:
            node = q.popleft()
            res.append(node)
            if node[0].left:
                q.append([node[0].left, node[1]+1])
            if node[0].right:
                q.append([node[0].right, node[1]+1])
        
        final_layer = res[-1][1]
        self.cur_stage = 0
        
        for i in range(final_layer+1):
            cur_res = []
            for j in range(self.cur_stage, len(res)):
                if res[j][1] == i:
                    cur_res.append(res[j][0].val)
                    self.cur_stage = j+1
            final_res.append(float(sum(cur_res)) / len(cur_res))
        
        return final_res
                    
 
# Method II:

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        self.res = []
        self.dfs(root, 0)
        final_res = [x/y for x, y in self.res]
        return final_res
        
    def dfs(self, root, layer):
        if root:
            if len(self.res)-1 < layer:
                self.res.append([0.0, 0])
            self.res[layer][0] += root.val
            self.res[layer][1] += 1
            self.dfs(root.left, layer+1)
            self.dfs(root.right, layer+1)
        
        
        
        
        
