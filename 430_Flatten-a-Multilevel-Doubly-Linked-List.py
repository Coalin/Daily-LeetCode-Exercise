"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def __init__(self):
        self.stack = []
        self.res = []
    
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        self.dfs(head)

        while self.stack:
            cur_node = self.stack.pop()
            if self.stack:
                self.stack[-1].next = cur_node
                cur_node.prev = self.stack[-1]
        return cur_node
            
        
    def dfs(self, head):
        if head:
            self.stack.append(Node(val=head.val, prev=None, next=None, child=None))
            self.dfs(head.child)
            self.dfs(head.next)

        
        
