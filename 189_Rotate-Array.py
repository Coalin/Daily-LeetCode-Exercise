class Solution:    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """   
        if not (k == 0 or len(nums) == 1):
            move = k%len(nums)
            save = nums[-move:]
            for i in reversed(range(move, len(nums))):
                nums[i] = nums[i-move]
            for j in range(move):
                nums[j] = save[j]
        
            

                    
        
        
