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


# Exercise III:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return 

        pre_node = ListNode(0)
        cur_node = ListNode(0)
        reset_node_1 = ListNode(0)
        reset_node_2 = ListNode(0)
        res_node = ListNode(0)

        cur_node.next = head
        pre_node.next = head
        res_node.next = head
        reset_node_1.next = head

        for _ in range(left):
            cur_node = cur_node.next
        
        for _ in range(left-1):
            pre_node = pre_node.next

        for _ in range(left-1):
            reset_node_1 = reset_node_1.next

        reset_node_2 = reset_node_1.next 

        for _ in range(left-1, right):
            next_node = cur_node.next 
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node

        reset_node_1.next = pre_node 
        reset_node_2.next = cur_node

        if left == 1:
            return reset_node_1.next 
        return res_node.next
