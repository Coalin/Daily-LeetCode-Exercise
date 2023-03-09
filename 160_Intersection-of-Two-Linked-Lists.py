# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        lenA = lenB = 0
        newA = headA
        newB = headB
        while headA:
            lenA += 1
            headA = headA.next
        while headB:
            lenB += 1
            headB = headB.next
        headA = newA
        headB = newB
        if lenA > lenB:
            for _ in range(lenA-lenB):
                headA = headA.next
        elif lenA < lenB:
            for _ in range(lenB-lenA):
                headB = headB.next
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        if not headA:
            return None
        else:
            return headA
        

# Exercise II:
# Mar 9, 2023
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p_a = headA 
        p_b = headB 
        len_a = len_b = 0

        while p_a:
            len_a += 1 
            p_a = p_a.next 

        while p_b:
            len_b += 1 
            p_b = p_b.next 

        if len_a > len_b:
            for _ in range(len_a-len_b):
                headA = headA.next 
        elif len_a < len_b:
            for _ in range(len_b-len_a):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next 
                headB = headB.next  

        return None
            
