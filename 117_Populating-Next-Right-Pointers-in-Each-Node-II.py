# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        head = None
        previous = None
        current = root
        while current:
            while current:
                if current.left:
                    if not previous:
                        head = current.left
                    else:
                        previous.next = current.left
                    previous = current.left
                if current.right:
                    if not previous:
                        head = current.right
                    else:
                        previous.next = current.right
                    previous = current.right
                current = current.next
            current = head
            previous = None
            head = None
        
            
# Exercise II:
# Feb 3, 2024
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 

        queue = [root]

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)
                if i < size-1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
