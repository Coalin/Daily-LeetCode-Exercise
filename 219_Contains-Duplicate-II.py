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
        
