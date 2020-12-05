# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.countLeft(root)
        right = self.countRight(root)
        if left == right:
            return 2**left-1
        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1
        
    def countLeft(self, root):
        count = 0
        while root:
            count += 1
            root = root.left
        return count
    
    def countRight(self, root):
        count = 0
        while root:
            count += 1
            root = root.right
        return count


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left)+self.countNodes(root.right)+1
        
