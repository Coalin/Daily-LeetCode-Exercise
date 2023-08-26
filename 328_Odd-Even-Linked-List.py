# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first = head
        second = head.next
        new_first = first
        new_second = second
        while first and first.next and second and second.next:
            first.next = first.next.next
            first = first.next
            second.next = second.next.next
            second = second.next
        first.next = new_second
        if second:
            second.next = None
        return new_first
            
            
# Exercise II:
# Aug 9, 2023
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
            
        even_head = head.next 
        even = even_head 
        odd = head 

        while even and even.next:
            odd.next = even.next 
            odd = odd.next 
            even.next = odd.next 
            even = even.next 

        odd.next = even_head

        return head        
