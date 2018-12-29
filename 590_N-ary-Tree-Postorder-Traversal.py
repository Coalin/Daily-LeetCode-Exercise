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
    
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root:
            for i in root.children:
                self.postorder(i)
            self.res.append(root.val)
        return self.res
        
