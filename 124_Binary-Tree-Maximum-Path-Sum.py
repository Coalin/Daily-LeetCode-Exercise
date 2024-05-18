# Exercise I:
# May 18, 2024
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        final_max = float('-inf')

        def nodeMaxSum(node):
            nonlocal final_max
            if not node:
                return 0 
            left_max = max(nodeMaxSum(node.left), 0)
            right_max = max(nodeMaxSum(node.right), 0)
            cur_max = node.val + left_max + right_max 
            final_max = max(final_max, cur_max)
            return node.val + max(left_max, right_max)

        nodeMaxSum(root)
        return final_max