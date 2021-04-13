# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = []

    def minDiffInBST(self, root: TreeNode) -> int:
        self._minDiffInBST(root)

        res = 2**32-1
        for i in range(1, len(self.output)):
            res = min(res, self.output[i]-self.output[i-1])

        return res

    def _minDiffInBST(self, root: TreeNode) -> int:
        if root:
            if root.left:
                self._minDiffInBST(root.left)
            self.output.append(root.val)
            if root.right:
                self._minDiffInBST(root.right)
                