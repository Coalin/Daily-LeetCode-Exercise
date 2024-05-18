# Exercise I:
# May 9, 2024
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, pathSum):
            if not root.left and not root.right:
                return pathSum*10+root.val 
            
            pathSum = pathSum*10+root.val 
            
            total_sum = 0 
            if root.left:
                total_sum += dfs(root.left, pathSum)
            if root.right:
                total_sum += dfs(root.right, pathSum)

            return total_sum

        return dfs(root, 0)
s