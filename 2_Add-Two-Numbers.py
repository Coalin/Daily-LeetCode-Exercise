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


# Exercise II:
# Dec 28, 2023
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_flag = 0 
        left = l1
        right = l2 
        res_head = ListNode(0)
        res = res_head

        while left and right:
            cur_num = (left.val+right.val+cur_flag)%10
            cur_flag = (left.val+right.val+cur_flag)//10
            res.next = ListNode(cur_num)
            left = left.next
            right = right.next
            res = res.next

        while left:
            cur_num = (left.val+cur_flag)%10
            cur_flag = (left.val+cur_flag)//10
            res.next = ListNode(cur_num)
            left = left.next
            res = res.next

        while right:
            cur_num = (right.val+cur_flag)%10
            cur_flag = (right.val+cur_flag)//10
            res.next = ListNode(cur_num)
            right = right.next
            res = res.next

        if cur_flag == 1:
            res.next = ListNode(1)
            res = res.next

        return res_head.next
