# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return abs(self.findSum(root.left)-self.findSum(root.right))+self.findTilt(root.left)+self.findTilt(root.right)
    
    def findSum(self, root):
        if not root:
            return 0
        return self.findSum(root.left)+self.findSum(root.right)+root.val
        
