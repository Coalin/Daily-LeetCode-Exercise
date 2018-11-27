# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        new_head = head
        fast = head
        slow = head
        count = 0
        
        while head:
            count += 1
            head = head.next
            
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        secondStart = self.reverseList(slow.next)
        
        if count%2 == 0:
            slow.next = None
        else:
            slow == None 
            
        while new_head and secondStart:
            if new_head.val != secondStart.val:
                return False
            else:
                new_head = new_head.next
                secondStart = secondStart.next
        return True
                
    
    def reverseList(self, head):
        pre = cur = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return cur
        
        
