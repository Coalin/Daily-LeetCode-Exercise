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
