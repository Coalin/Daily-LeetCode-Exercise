# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        q = deque()
        q.append([root, 0])
        res = []
        final_res = []
        
        while q:
            node = q.popleft()
            res.append(node)
            if node[0].left:
                q.append([node[0].left, node[1]+1])
            if node[0].right:
                q.append([node[0].right, node[1]+1])
        
        for i in range(len(res)-1):
            if res[i][1] != res[i+1][1]:
                final_res.append(res[i][0].val)
        
        final_res.append(res[-1][0].val)
        
        return final_res
            

# Exercise II:
# Feb 12, 2024
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            # 由于在循环中使用了 queue.pop(0)，这会导致 len(queue) 的值在循环过程中发生变化，从而导致判断条件不准确。
            # 正确的做法是在进入循环之前获取当前队列的长度，并在循环中使用这个固定的长度值。
            queue_len = len(queue)
            for i in range(queue_len):
                cur_node = queue.pop(0)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                if i == queue_len - 1:
                    res.append(cur_node.val)

        return res 
