# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root        
        self.sort_res = []
        self.middleSearch(root, self.sort_res)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.sort_res      
        
        
    def next(self):
        """
        :rtype: int
        """
        if not self.sort_res:
            return None
        return self.sort_res.pop()
        
    
    def middleSearch(self, root, res):
        if root:
            self.middleSearch(root.right, res)
            res.append(root.val)
            self.middleSearch(root.left, res)
        
        
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
