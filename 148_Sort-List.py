# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None:
            return head
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res = sorted(res)
        head = ListNode(res[0])
        new_head = head
        for i in range(1, len(res)):
            new_node = ListNode(res[i])
            head.next = new_node
            head = head.next
        head.next = None
        return new_head
            
        
        
