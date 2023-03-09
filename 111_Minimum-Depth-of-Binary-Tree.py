# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and not root.right:
            return self.minDepth(root.left)+1
        elif root.right and not root.left:
            return self.minDepth(root.right)+1
        elif root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
        else:
            return 1
        
# Exercise II 
# Aug 23, 2020 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1 
        if root.left is None:
            return self.minDepth(root.right)+1
        if root.right is None:
            return self.minDepth(root.left)+1
        
        return min(self.minDepth(root.left), self.minDepth(root.right))+1


# Exercise III:
# Mar 2, 2023
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and root.right:
            return self.minDepth(root.right)+1
        if not root.right and root.left:
            return self.minDepth(root.left)+1 
        
        return min(self.minDepth(root.left), self.minDepth(root.right))+1
