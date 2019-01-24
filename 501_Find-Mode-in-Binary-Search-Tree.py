# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res_dic = dict()
        final_count = 0
        final_res = []
        
        self.inorder(root)
        
        for i in self.res:
            if i in res_dic:
                res_dic[i] += 1
            else:
                res_dic[i] = 1
                
        for j in res_dic:
            final_count = max(final_count, res_dic[j])
            
        for x in res_dic:
            if res_dic[x] == final_count:
                final_res.append(x)
            
        return final_res
        
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.res.append(root.val)
            self.inorder(root.right)
        
