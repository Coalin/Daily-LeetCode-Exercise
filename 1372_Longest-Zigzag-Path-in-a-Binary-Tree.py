# Exercise I:
# Sep 6, 2023

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.dfs(root, 'left', 0)
        self.dfs(root, 'right', 0)
        
        return self.res
        
    def dfs(self, root, direction, length):
        if not root:
            return 

        self.res = max(length, self.res)

        if direction == 'left':
            self.dfs(root.left, 'right', length+1)
            self.dfs(root.right, 'left', 1)
        else:
            self.dfs(root.right, 'left', length+1)
            self.dfs(root.left, 'right', 1)
        
        return length
