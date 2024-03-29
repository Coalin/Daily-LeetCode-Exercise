# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Method I: by building a new single-linked list
        # 构建一个新的链表头，然后遍历时直接将链表元素加入到新链接中
        new_head = None
        while head:
            p = head
            head = head.next    # 这一步的位置不能改！！！
            p.next = new_head
            new_head = p
        return new_head
    
        # Method II: 遍历时直接将指针反转
        # 48 ms, 99.42%.
        cur = None 
        pre = None 
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return cur

        
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        post = head.next
        head.next = None
        while post != None:
            pre = head
            head = post
            post = head.next            
            head.next = pre
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head 
        if not head.next:
            return head

        pre_node = None
        cur_node = head

        while cur_node:
            # 保存
            tmp_node = cur_node.next
            # 反转
            cur_node.next = pre_node
            # 迭代
            pre_node = cur_node
            cur_node = tmp_node
            
        return pre_node