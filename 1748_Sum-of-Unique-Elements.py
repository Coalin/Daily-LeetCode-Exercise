class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        my_dict = {}
        res = 0

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        for key in my_dict:
            if my_dict[key] == 1:
                res += key 
        
        return res
