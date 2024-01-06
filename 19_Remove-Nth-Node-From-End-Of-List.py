# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        fast = slow = new_head
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        #fast.next = fast.next.next
        return new_head.next

# 定义双指针Fast与Slow，Fast先走
# 定义一个新的head


# Exercise II:
# Jan 6, 2024
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0)
        start.next = head 
        res = start
        fast = head 
        idx = 0
        cnt = 0

        while fast:
            cnt += 1
            fast = fast.next

        while start:
            if idx == cnt-n:
                start.next = start.next.next  
            start = start.next
            idx += 1 

        return res.next
