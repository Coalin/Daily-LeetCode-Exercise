"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        start = Node(0)
        start.next = head

        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        if head.next == head:
            new_node_0 = Node(insertVal)
            head.next = new_node_0
            new_node_0.next = head 
            return start.next

        cur = head 
        nex = cur.next 
       
        while cur.val <= nex.val:
            cur = cur.next 
            nex = cur.next 
            if nex == head:
                break 
        real_head = nex

        while nex.val <= insertVal:
            cur = cur.next 
            nex = cur.next 
            if nex == real_head:
                break
        
        new_node_1 = Node(insertVal)
        cur.next = new_node_1
        new_node_1.next = nex 

        return start.next
