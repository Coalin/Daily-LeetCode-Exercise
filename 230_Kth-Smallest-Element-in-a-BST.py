# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        path = []
        self.orderPath(root, path)
        return path[k-1]
    
    def orderPath(self, root, path):
        if root is not None:
            self.orderPath(root.left, path)
            path.append(root.val)
            self.orderPath(root.right, path)
    
        
        
