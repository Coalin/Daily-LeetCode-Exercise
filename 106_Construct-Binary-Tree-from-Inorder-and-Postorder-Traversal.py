# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        node = postorder.pop()
        root = TreeNode(node)
        index = inorder.index(node)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:])
        return root
        

# Exercise II:
# Feb 3, 2024
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return

        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):len(postorder)-1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root
