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


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        mid_res = []
        res = []
        cur_res = [str(nums[0])]

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                cur_res.append(str(nums[i]))
            else:
                mid_res.append(cur_res)
                cur_res = [str(nums[i])]

        mid_res.append(cur_res)
        print(mid_res)

        for item in mid_res:
            if len(item) == 1:
                res.append(item[0])
            else:
                res.append(str(item[0])+'->'+str(item[-1]))

        return res 


# Exercise III:
# Dec 25, 2023
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        i = 0 
        while i < len(nums):
            left = nums[i]
            while i+1 < len(nums) and nums[i+1] == nums[i]+1:
                i += 1
            right = nums[i]
            if left == right:
                res.append(str(left))
            else:
                res.append(str(left)+'->'+str(right))
            i += 1

        return res
   