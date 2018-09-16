# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return 
        head = ListNode(0)
        new_list = head
        K = len(lists)
        res = lists[0]
        for i in range(1, K):
            res = self.mergeTwoLists(res, lists[i])
        return res
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_list = new_head
        while l1 and l2:
            if l1.val < l2.val:
                new_head.next = l1
                l1 = l1.next
            else:
                new_head.next = l2
                l2 = l2.next
            new_head = new_head.next
        if l1:
            new_head.next = l1
        if l2:
            new_head.next = l2
        return new_list.next 
   
# 12.10%; 5,508ms.
