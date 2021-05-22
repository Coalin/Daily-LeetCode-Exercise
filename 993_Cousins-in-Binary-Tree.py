# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_depth = None 
        x_parent = None 
        x_found = 0
        y_depth = None 
        y_parent = None 
        y_found  = 0

        def dfs(node, parent, depth):
            nonlocal x_depth, x_parent, x_found, y_depth, y_found, y_parent
            if not node:
                return 
            if node.val == x:
                x_depth = depth 
                x_parent = parent 
                x_found = 1 
            elif node.val == y:
                y_depth = depth 
                y_parent = parent 
                y_found = 1 
            if x_found and y_found:
                return 
            dfs(node.left, node, depth+1)
            if x_found and y_found:
                return 
            dfs(node.right, node, depth+1)
        
        dfs(root, None, 0)
        return x_depth == y_depth and x_parent != y_parent 
