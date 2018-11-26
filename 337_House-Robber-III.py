# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method I:
class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.includeRoot(root), self.excludeRoot(root))
        
    def includeRoot(self, root):
        if not root:
            return 0
        return root.val+self.excludeRoot(root.left)+self.excludeRoot(root.right)
    
    def excludeRoot(self, root):
        if not root:
            return 0
        return self.rob(root.left)+self.rob(root.right)
 
 # Method II:
 class Solution:
    def rob(self, root):
        if not root:
            return 0
        val = 0
        if root.left:
            val += (self.rob(root.left.left)+self.rob(root.left.right))
        if root.right:
            val += (self.rob(root.right.left)+self.rob(root.right.right))
        return max(root.val+val, self.rob(root.left)+self.rob(root.right))
 
