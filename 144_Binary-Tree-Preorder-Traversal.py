# Method I:

# 64ms, 9.74%.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preTraversal(root, res)
        return res
        
    def preTraversal(self, root, res):
        if root:
            res.append(root.val)
            self.preTraversal(root.left, res)
            self.preTraversal(root.right, res)
       
# Method II:

# 56ms, 18.15%

class Solution:
    def __init__(self):
        self.res = []
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.res
    
# Method III:

# 44ms, 97.93%

class Solution:
    def preorderTraversal(self, root):
        res = []
        stack = []
        if not root:
            return res
        stack.append(root)
        while stack:
            pop = stack.pop()
            res.append(pop.val)
            if pop.right:
                stack.append(pop.right)
            if pop.left:
                stack.append(pop.left)
        return res
