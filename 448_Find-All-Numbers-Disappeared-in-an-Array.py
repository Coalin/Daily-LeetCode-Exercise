class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_ = len(nums)
        nums = list(set(nums))
        num_dic = {}
        res = []
        
        for i in nums:
            num_dic[i] = 1
        for i in range(1, len_+1):
            if i not in num_dic:
                res.append(i)
        return res
        
        
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        
        my_hash_table = dict()
        for num in nums:
            if num in my_hash_table:
                my_hash_table[num] += 1
            else:
                my_hash_table[num] = 1
        
        for k in range(1, n+1):
            if k not in my_hash_table:
                res.append(k)

        return res