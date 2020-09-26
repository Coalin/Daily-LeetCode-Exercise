# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.dfs(root, res, sum, path=[])
        return res

    def dfs(self, root, res, sum, path):
        if not root:
            return 
        if root.left is None and root.right is None:
            if root.val == sum:
                path += [root.val]
                res.append(path)
                return 
        self.dfs(root.left, res, sum-root.val, path+[root.val])
        self.dfs(root.right, res, sum-root.val, path+[root.val])
