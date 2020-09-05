# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.paths = []
        self.dfs(root, '')
        return self.paths

    def dfs(self, root, path):
        if root:
            # 如果为叶子节点
            path += str(root.val)
            if not root.left and not root.right: 
                self.paths.append(path)
            else:
                path += ('->')
                self.dfs(root.left, path)
                self.dfs(root.right, path)
