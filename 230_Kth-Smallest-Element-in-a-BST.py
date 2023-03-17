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
    
        
# Exercise II
# Mar 17, 2023
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        self.inorder(root)
        return self.res[k-1]

    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

