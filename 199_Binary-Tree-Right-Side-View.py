# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        q = deque()
        q.append([root, 0])
        res = []
        final_res = []
        
        while q:
            node = q.popleft()
            res.append(node)
            if node[0].left:
                q.append([node[0].left, node[1]+1])
            if node[0].right:
                q.append([node[0].right, node[1]+1])
        
        for i in range(len(res)-1):
            if res[i][1] != res[i+1][1]:
                final_res.append(res[i][0].val)
        
        final_res.append(res[-1][0].val)
        
        return final_res
            
            
        
