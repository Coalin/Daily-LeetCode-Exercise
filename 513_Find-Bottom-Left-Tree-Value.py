# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tree_hash = dict()
        q = deque()
        q.append([1, root])
        depth = self.maxDepth(root)
        
        while q:
            node = q.popleft()
            if node[0] == depth:
                return node[1].val
            if node[0] not in tree_hash:
                tree_hash[node[0]] = [node[1]]
            else:
                tree_hash[node[0]].append(node[1])
            if node[1].left:
                q.append([node[0]+1, node[1].left])
            if node[1].right:
                q.append([node[0]+1, node[1].right])
        
        
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

        
        
