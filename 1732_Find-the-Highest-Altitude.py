class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_height = 0
        max_height = 0

        for i in range(len(gain)):
            cur_height = cur_height + gain[i]
            max_height = max(cur_height, max_height)

        return max_height
