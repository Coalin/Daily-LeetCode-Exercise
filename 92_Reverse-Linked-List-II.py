# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        stack[m-1:n] = reversed(stack[m-1:n])
        first = ListNode(0)
        res = first
        while stack:
            first.next = ListNode(stack.pop(0))
            first = first.next
        return res.next
    
# Exercise II:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        
        if m == 1:
            p1 = None
            p2 = head
            
        elif m >= 2:
            p1 = head
            p1_ = p1
            p2 = head
            for _ in range(m-2):
                p1_ = p1_.next
            p2 = p1_.next
        
        p3 = p2
        for _ in range(n-m+1):
            p3 = p3.next
        
        pre = p3
        cur = p2
        
        for _ in range(m-1, n):
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        
        if p1:
            p1_.next = pre
            return p1
        else:
            return pre
        
        
