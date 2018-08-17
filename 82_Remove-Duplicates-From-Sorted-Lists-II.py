# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        exist = []
        dup = []
        new_head = ListNode(0)
        new_head.next = head
        pre = new_head
        while head:
            if head.val in exist:
                dup.append(head.val)
            else:
                exist.append(head.val)
            head = head.next
        cur = pre.next
        new_head.next = cur
        while cur:
            if cur.val in dup:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return new_head.next
 
 # 第一次提交出错的原因：
 # 第二个while中仍使用了head，而head早已走到了最后
