# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        exist = []
        pre = new_head = ListNode(0)
        new_head.next = head
        while head:
            if head.val in exist:
                pre.next = head.next
                head = head.next
            else:
                exist.append(head.val)
                pre = head
                head = head.next
        return new_head.next
                
                
            
