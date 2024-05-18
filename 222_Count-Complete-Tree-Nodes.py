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
        

# Exercise III:
# Feb 4, 2024
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        if left_height == right_height:
            return 2 ** left_height + self.countNodes(root.right)
        else:
            return 2 ** right_height + self.countNodes(root.left)

    def get_height(self, root):
        if not root:
            return 0 
            
        res = 0
        while root:
            res += 1
            root = root.left 

        return res
