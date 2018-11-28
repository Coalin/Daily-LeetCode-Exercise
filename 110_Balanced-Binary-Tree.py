# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if self.balance(root) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
    
    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right))+1
    
    def balance(self, root):
        if not root:
            return True
        if abs(self.height(root.left)-self.height(root.right)) <= 1:
            return True
        else:
            return False
        
