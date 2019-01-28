# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        preorder = deque(preorder)
        node = preorder.popleft()
        root = TreeNode(node)
        index = inorder.index(node)
        root.left = self.buildTree(list(preorder)[:index], inorder[:index])
        root.right = self.buildTree(list(preorder)[index:], inorder[index+1:])
        return root
        
