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
