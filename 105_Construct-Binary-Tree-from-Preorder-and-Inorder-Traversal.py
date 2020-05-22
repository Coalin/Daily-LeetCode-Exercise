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


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 前序-根左右
        # 中序-左根右
        
        # 根节点
        if not preorder:
            return None
        x = preorder.pop(0)
        root = TreeNode(x)
        
        # 根节点在中序遍历中的index，左为左子树，右为右子树
        i = inorder.index(x)

        # 前序遍历中，前i个为左子树
        root.left = self.buildTree(preorder[:i], inorder[:i])
        root.right = self.buildTree(preorder[i:], inorder[i+1:])

        return root
