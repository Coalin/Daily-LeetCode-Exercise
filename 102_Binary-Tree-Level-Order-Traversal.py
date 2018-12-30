# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = {}
        final_res = []
        q = deque()
        q.append([0, root])
        
        while q:
            node = q.popleft()
            if node[0] in res:
                res[node[0]].append(node[1].val)
            else:
                res[node[0]] = [node[1].val]
            if node[1].left:
                q.append([node[0]+1, node[1].left])
            if node[1].right:
                q.append([node[0]+1, node[1].right])
        for i in res:
            final_res.append(res[i])
        
        return final_res
        
        
        
