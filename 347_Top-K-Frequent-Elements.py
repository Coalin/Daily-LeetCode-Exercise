class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_dic = {}
        res = []
        final_res = []
        for item in nums:
            if item in num_dic:
                num_dic[item] += 1
            else:
                num_dic[item] = 1
        for key, val in num_dic.items():
            res.append([key, val])
        res = sorted(res, key=lambda x: x[1], reverse=True)
        for i in res:
            final_res.append(i[0])
        return final_res[:k]


# Sep 7, 2020
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        res = sorted(dic.items(),key = lambda x:x[1], reverse = True)

        final = []
        for arr in res[:k]:
            final.append(arr[0])

        return final
