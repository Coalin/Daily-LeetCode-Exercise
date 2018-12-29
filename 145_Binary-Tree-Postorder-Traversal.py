# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.res.append(root.val)
        return self.res
    
class Solution(object):
    def __init__(self):
        self.res = []
        self.stack = []
    
    def postorderTraversal(self, root):
        if not root:
            return []
        
        self.stack.append(root)
        while self.stack:
            node = self.stack.pop()
            self.res.append(node.val)
            if node.left:
                self.stack.append(node.left)
            if node.right:
                self.stack.append(node.right)
        
        return self.res[::-1]
            
        
        
