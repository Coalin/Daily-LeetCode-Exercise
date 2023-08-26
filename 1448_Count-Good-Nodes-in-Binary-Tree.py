# Exercise I:
# Aug 26, 2023

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -2**31)

    def dfs(self, root, path_max):
        res = 0 
        if not root:
            return 0 
        if root.val >= path_max:
            res += 1
            path_max = root.val 
        res += self.dfs(root.left, path_max)
        res += self.dfs(root.right, path_max)
        return res
        