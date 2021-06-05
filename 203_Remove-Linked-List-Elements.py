# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        while head:
            if head.val == val:
                head = head.next 
            else:
                break 

        pre = ListNode(0)
        res = ListNode(0)
        pre.next = head
        res.next = head
        cur = head

        while cur:
            if cur.val == val:
                pre.next = cur.next 
                cur = cur.next  

            else:
                pre = cur 
                cur = cur.next  
        
        return res.next 
