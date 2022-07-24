class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = dict()
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if temp.has_key(num):
                temp[num] += 1
                if temp[num] > len(nums)/2:
                    return num
            else:
                temp[num] = 1


# 摩尔投票
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        cnt = 0
        
        for i in range(len(nums)):
            if maj == nums[i]:
                cnt += 1
            elif maj != nums[i]:
                cnt -= 1 
                if cnt == 0:
                    maj = nums[i]
                    cnt += 1

        return maj
