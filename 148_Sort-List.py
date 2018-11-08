# Method I:

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

# method II: Merge Sort

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        middle = self.findMiddle(head)
        left = head
        right = middle.next
        middle.next = None
        return self.mergeTwoLists(self.sortList(left), self.sortList(right))
        
        
    def findMiddle(self, head):
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        stored_head = new_head
        while l1 and l2:
            if l1.val<=l2.val:
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
        return stored_head.next
        
        
            
        
        
