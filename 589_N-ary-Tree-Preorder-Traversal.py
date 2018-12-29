"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def __init__(self):
        self.res = []
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root:
            self.res.append(root.val)
            for i in root.children:
                self.preorder(i)
        return self.res
        
