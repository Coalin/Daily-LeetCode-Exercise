class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # if not nums:
        #     return False
        # if k == 0:
        #     return False
        # for i in range(len(nums)-1):
        #     for j in range(i+1, min(i+k+1, len(nums))):
        #         if abs(nums[i]-nums[j]) <= t:
        #             print(i, j, abs(nums[i]-nums[j]))
        #             return True
        # return False
        
        if not nums:
            return False
        if k == 0:
            return False
        set_a = set()
        for i in range(len(nums)):
            if t == 0:
                if nums[i] in set_a:
                    return True
            else:
                for item in set_a:
                    if abs(nums[i]-item) <= t:
                        return True
            if len(set_a) == k:
                set_a.remove(nums[i-k])
            set_a.add(nums[i])
        return False

                
        
