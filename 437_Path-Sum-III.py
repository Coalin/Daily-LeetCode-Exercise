# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.tree_node = []
        self.res = 0
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.traversal(root)
        for i in self.tree_node:
            self.res += self._pathSum(i, sum)
        return self.res
        
    def traversal(self, root):
        if root:
            self.traversal(root.left)
            self.tree_node.append(root)
            self.traversal(root.right)
                    
    def _pathSum(self, root, sum):
        if not root:
            return 0
        if root.val == sum:
            return 1+self._pathSum(root.left, 0)+self._pathSum(root.right, 0)
        return self._pathSum(root.left, sum-root.val)+self._pathSum(root.right, sum-root.val)
        
