# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        new_head = pre = ListNode(0)
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = head
            pre.next = temp
            pre = head
            head = head.next
        return new_head.next
            
