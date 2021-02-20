class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hash_table_1 = {}
        for i in range(len(nums)):
            if nums[i] in hash_table_1:
                hash_table_1[nums[i]].append(i)
            else:
                hash_table_1[nums[i]] = [i]

        hash_table_2 = {}
        for key, val in hash_table_1.items():
            hash_table_2[key] = len(hash_table_1[key])

        hash_table_3 = {}
        max_val = 0
        for key, val in hash_table_2.items():
            if val in hash_table_3:
                hash_table_3[val].append(key)
            else:
                hash_table_3[val] = [key]
            max_val = max(max_val, val)

        res = len(nums)
        for i in hash_table_3[max_val]:
            res = min(res, max(hash_table_1[i])-min(hash_table_1[i])+1)

        return res 
