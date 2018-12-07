# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def isValidBSTRoot(self, root):
        if root:
            self.isValidBSTRoot(root.left)
            self.res.append(root.val)
            self.isValidBSTRoot(root.right)
            
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            self.isValidBSTRoot(root)
        return sorted(self.res) == self.res and len(set(self.res)) == len(self.res)

        

        
