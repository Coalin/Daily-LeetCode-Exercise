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

        
# Exercise II:
# Mar 25, 2023
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.inorder(root, res)

        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        
        return True

    def inorder(self, root, res):
        if not root:
            return 

        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
