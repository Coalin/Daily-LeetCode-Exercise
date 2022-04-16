# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0

        def depth_of_bst(root):
            if not root:
                return 0
            L = depth_of_bst(root.left)
            R = depth_of_bst(root.right)
            self.res = max(L+R+1, self.res)
            return max(L, R)+1

        depth_of_bst(root)

        return self.res-1
