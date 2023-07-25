# Exercise I:
# July 25, 2023

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None 
            
        start = ListNode(0)
        start.next = head 
        copy = start

        cnt = 0 
        while start.next:
            start = start.next 
            cnt += 1

        idx = cnt//2

        for _ in range(idx):
            copy = copy.next 
            
        new = copy.next.next
        copy.next = new 

        return head
