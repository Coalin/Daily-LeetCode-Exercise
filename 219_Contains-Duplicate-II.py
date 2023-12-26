class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or k == 0:
            return False
        set_a = set()
        for i in range(len(nums)):
            if nums[i] in set_a:
                return True
            if len(set_a) == k:
                set_a.remove(nums[i-k])
            set_a.add(nums[i])
        return False
        

# Exercise II:
# Dec 23, 2023
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res_dict = dict()

        for i in range(len(nums)):
            if nums[i] in res_dict:
                res_dict[nums[i]].append(i)
            else:
                res_dict[nums[i]] = [i] 

        for m in res_dict:
            if len(res_dict[m]) > 1:
                for j in range(len(res_dict[m])-1):
                    if res_dict[m][j+1] - res_dict[m][j] <= k:
                        return True
        
        return False
