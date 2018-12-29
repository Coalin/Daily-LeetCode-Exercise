"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = {}
        queue = deque()
        final_res = []
        
        if not root:
            return []
        queue.append([root, 0])
        
        while queue:
            node = queue.popleft()
            if node[1] not in res:
                res[node[1]] = [node[0].val]
            else:
                res[node[1]].append(node[0].val)
            if node[0].children:
                for i in node[0].children:
                    queue.append([i, node[1]+1])
        
        for i in res:
            final_res.append(res[i])
            
        return final_res
        
