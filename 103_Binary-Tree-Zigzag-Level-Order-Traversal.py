# Exercise I:
# Feb 12, 2024
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]
        cnt = 0

        while queue:
            cur_list = []
            queue_len = len(queue)
            cnt += 1
            for i in range(queue_len):
                cur_node = queue.pop(0)
                cur_list.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                if i == queue_len-1:
                    if cnt % 2 == 1:
                        res.append(cur_list)
                    else:
                        res.append(cur_list[::-1])
                    cur_list = []

        return res
            