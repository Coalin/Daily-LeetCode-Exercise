# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.symmetric(root.left, root.right)
        
    def symmetric(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        else:
            if self.symmetric(root1.left, root2.right) and self.symmetric(root1.right, root2.left):
                return True
        return False
        

# Exercise II:
# Apr 8, 2023
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isTwoSymmetric(root.left, root.right)
    
    def isTwoSymmetric(self, root1, root2):
        if not root1 and not root2:
            return True 
        if (root1 and not root2) or (root2 and not root1):
            return False
        if root1.val != root2.val:
            return False
        return self.isTwoSymmetric(root1.left, root2.right) and self.isTwoSymmetric(root1.right, root2.left)
