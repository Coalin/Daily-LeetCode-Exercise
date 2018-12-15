class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 1:
            return [str(nums[0])]
        
        res = []
        final_res = []
        left = 0
        right = 0
        
        while right < len(nums)-1:
            if nums[right+1] == nums[right]+1:
                right += 1
            else:
                res.append(nums[left:right+1])
                left = right + 1
                right = right + 1
            if right == len(nums)-1:
                res.append(nums[left:]) 
                
        for i in res:
            if len(i) == 1:
                final_res.append(str(i[0]))
            else:
                final_res.append(str(i[0])+'->'+str(i[-1]))
                
        return final_res
        
