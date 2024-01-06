# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
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
            
# 66.35%; 64ms.  


# Exercise II 
# 31 Dec, 2022
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0)
        res = start

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                start.next = list1
                list1 = list1.next 
            else:
                start.next = list2
                list2 = list2.next 
            start = start.next 

        if list1 is not None:
            start.next = list1 
        if list2 is not None:
            start.next = list2 

        return res.next


# Exercise III:
# Dec 28, 2023
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        res_head = res 

        while list1 and list2:
            if list1.val < list2.val:
                res.next = ListNode(list1.val)
                list1 = list1.next 
            else:
                res.next = ListNode(list2.val)
                list2 = list2.next 
            res = res.next

        if list1:
            res.next = list1 
        if list2:
            res.next = list2 

        return res_head.next
