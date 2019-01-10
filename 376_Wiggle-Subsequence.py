# Method I: DFS; 超出时间限制
# class Solution:
#     def wiggleMaxLength(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         self.res = 0
#         self.dfs(nums, 0, [],)
#         return self.res
        

#     def dfs(self, nums, index, path):
#         for i in range(index, len(nums)):
#             if len(path) == 0:
#                 path += [nums[i]]
#             elif len(path) == 1:
#                 if path[0] != nums[i]:
#                     path += [nums[i]]
#             else:
#                 if (path[-1]-path[-2])*(nums[i]-path[-1]) < 0:
#                     path += [nums[i]]
#             self.res = max(self.res, len(path))
#             self.dfs(nums, i+1, path)
#             if path:
#                 path.pop()

# Method II: DP
class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        inc = [1 for _ in range(len(nums))]
        dec = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i], dec[j]+1)
                elif nums[i] < nums[j]:
                    dec[i] = max(dec[i], inc[j]+1)
        
        print(inc)
        print(dec)
                    
        return max(inc[-1], dec[-1])
                    
    
                
            
            
