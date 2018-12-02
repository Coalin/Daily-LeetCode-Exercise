# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method I:
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root        
        self.stack = []
        self.middleSearch(root, self.stack)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack     
        
        
    def next(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack.pop()
        
    
    def middleSearch(self, root, res):
        if root:
            self.middleSearch(root.right, res)
            res.append(root.val)
            self.middleSearch(root.left, res)
        
        
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# Method II:
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root        
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack     
        
        
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        right = node.right
        while right:
            self.stack.append(right)
            right = right.left
        return node.val
