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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0 
        self.localSum(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.res

    def localSum(self, root, Sum):
        if not root:
            return 
        Sum -= root.val
        if Sum == 0:
            self.res += 1
        self.localSum(root.left, Sum)
        self.localSum(root.right, Sum)
        

# Exercise III:
# Sep 2, 2023
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        res = self.pathSumRoot(root, targetSum)
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        return res

    def pathSumRoot(self, root, curSum):
        res = 0
        if not root:
            return 0
        curSum -= root.val
        if curSum == 0:
            res += 1
        res += self.pathSumRoot(root.left, curSum)
        res += self.pathSumRoot(root.right, curSum)
        return res
