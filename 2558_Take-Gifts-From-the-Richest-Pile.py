# Exercise I:
# Oct 28, 2023

from heapq import heapify, heappop, heappush

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-item for item in gifts]
        heapify(heap)

        while k:
            x = heappop(heap)
            heappush(heap, -int(sqrt(-x)))
            k -= 1

        return -sum(heap)