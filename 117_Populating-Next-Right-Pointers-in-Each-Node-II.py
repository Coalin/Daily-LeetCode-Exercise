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
        
            
            
                

                
            

        
