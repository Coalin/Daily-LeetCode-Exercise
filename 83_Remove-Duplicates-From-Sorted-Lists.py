# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return 

        first = ListNode(0)
        before = ListNode(0)
        first.next = head 
        before.next = head

        exists = []

        while head:
            if head.val in exists:
                before.next = head.next 
            else:
                before = before.next 
                exists.append(head.val)
            head = head.next 
        
        return first.next
