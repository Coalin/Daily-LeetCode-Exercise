# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
当遍历到一个root点的时候，

1.判断root是不是null. 如果root为null，那么就无所谓祖先节点，直接返回null就好了;

2.如果root的左子树存在p，右子树存在q，那么root肯定就是最近祖先;

3.如果pq都在root的左子树，那么就需要递归root的左子树，右子树同理。
"""

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None:
            return root
        elif left == None:
            return right
        else:
            return left
        

# Exercise II:
# Feb 13, 2023        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root 

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root 
        elif left is not None and right is None:
            return left 
        elif left is None and right is not None:
            return right 
        else:
            return None
