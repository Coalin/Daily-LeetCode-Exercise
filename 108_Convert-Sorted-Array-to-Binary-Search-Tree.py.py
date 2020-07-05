# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        middle_id = len(nums)//2
        res = TreeNode(nums[middle_id])
        res.left = self.sortedArrayToBST(nums[:middle_id])
        res.right = self.sortedArrayToBST(nums[middle_id+1:])

        return res 
