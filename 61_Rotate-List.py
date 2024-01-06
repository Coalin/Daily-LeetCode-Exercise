# Method I:
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
            
# Method II:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 0 or head.next == None:
            return head
        else:
            pointer = head
            count = 0
            while pointer:
                count += 1
                pointer = pointer.next
            for _ in range(k%count):
                head = self.rotateRightOne(head)
        return head
        
    def rotateRightOne(self, head):
        new_head = ListNode(0)
        new_head.next = head
        while head:
            if head.next.next == None:
                break
            else:
                head = head.next
        head_ = head.next
        head_.next = new_head.next
        new_head.next = head_
        head.next = None
        return new_head.next

# 22.25%; 76ms.

# Method III: Two Pointers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head:
            return head
        
        new_head = head
        
        count = 0
        while head:
            count += 1
            head = head.next
        k = k%count
        

        fast = new_head
        slow = new_head
        
        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        fast.next = new_head
        res = slow.next
        slow.next = None    
        
        return res
    

# Jan 6, 2024
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not k or not head:
            return head

        dummy = ListNode(0)
        dummy.next = head 

        p1 = dummy 
        cnt = 0

        while p1.next:
            p1 = p1.next 
            cnt += 1

        if not k%cnt:
            return head
        
        p2 = dummy
        for _ in range(cnt-k%cnt):
            p2 = p2.next 

        p3 = dummy
        p3.next = p2.next 
        p2.next = None
        p1.next = head 

        return p3.next
