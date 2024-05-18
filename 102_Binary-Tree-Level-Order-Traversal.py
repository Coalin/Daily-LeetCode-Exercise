# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = {}
        final_res = []
        q = deque()
        q.append([0, root])
        
        while q:
            node = q.popleft()
            if node[0] in res:
                res[node[0]].append(node[1].val)
            else:
                res[node[0]] = [node[1].val]
            if node[1].left:
                q.append([node[0]+1, node[1].left])
            if node[1].right:
                q.append([node[0]+1, node[1].right])
        for i in res:
            final_res.append(res[i])
        
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            cur_list = []
            queue_len = len(queue)
            for i in range(queue_len):
                cur_node = queue.pop(0)
                cur_list.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                if i == queue_len-1:
                    res.append(cur_list)
                    cur_list = []

        return res
