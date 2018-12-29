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

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                for i in reversed(range(len(node.children))):
                    stack.append(node.children[i])
        return res
