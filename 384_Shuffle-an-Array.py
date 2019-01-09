class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = copy.deepcopy(nums)
        self.initial = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.initial
        
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = []
        while self.nums:
            cur = self.nums[random.randint(0, len(self.nums)-1)]
            res.append(cur)
            self.nums.remove(cur)
        self.nums = copy.deepcopy(res)
        return self.nums
        
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
