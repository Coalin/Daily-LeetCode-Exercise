# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        temp = ListNode(0)
        res = temp
        flag = 0
        
        while l1 or l2:
            tempsum = 0
            if l1:
                tempsum = l1.val
                l1 = l1.next
            if l2:
                tempsum += l2.val
                l2 = l2.next
            tempres = (tempsum+flag)%10
            flag = (tempsum+flag)/10
            res.next = ListNode(tempres)
            res = res.next
        if flag:
            res.next = ListNode(1)
        res = temp.next
        del temp
        return res
