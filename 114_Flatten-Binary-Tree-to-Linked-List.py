# Exercise I:
# Feb 12, 2024
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 

        start = root 
        self.flatten(root.left)
        self.flatten(root.right)
        
        tmp = root.right
        root.right = root.left 
        root.left = None 

        while root.right:
            root = root.right 

        root.right = tmp 

        return root
