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
    
class Solution(object):
    def __init__(self):
        self.res = []
        self.stack = []
    
    def postorder(self, root):
        if not root:
            return []
        
        self.stack.append(root)
        
        while self.stack:
            node = self.stack.pop()
            self.res.append(node.val)
            if node.children:
                for i in node.children:
                    self.stack.append(i)
        
        return self.res[::-1]
        
