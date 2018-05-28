# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution I: Recursive
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.recursive(root, res)
        return res
    
    def recursive(self, root, res):
        if root:
            self.recursive(root.left, res)
            res.append(root.val)
            self.recursive(root.right, res)
