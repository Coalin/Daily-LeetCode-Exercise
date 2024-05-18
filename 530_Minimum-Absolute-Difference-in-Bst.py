# Exercise I:
# Jan 17, 2024
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = float('-inf')
        self.res = float('inf')

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        return self.res

    def inorder(self, root):
        if not root:
            return 
        
        self.inorder(root.left)
        self.res = min(root.val - self.pre, self.res)
        self.pre = root.val
        self.inorder(root.right)
