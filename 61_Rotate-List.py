# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 0:
            return head
        new_head = ListNode(0)
        new_head.next = head
        p = new_head
        count = 0
        while p.next != None:
            p = p.next
            count += 1
        p.next = new_head.next
        last = count - k%count
        p = new_head.next
        for _ in range(1, last):
            p = p.next
        head = p.next
        p.next = None
        return head

# 先把Linked List结成环形
# 这里head最后的位置是p.next，找到Rotation后的头结点并返回 
            
        
    

            
            
            
                
        
