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
        
