import heapq

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if len(arr) == 0:
            return []
        if k == 0:
            return []
        if k >= len(arr):
            return arr

        res = []
        arr_adverse = [-n for n in arr]
        hp = arr_adverse[:k]
        heapq.heapify(hp)

        for i in range(k, len(arr)):
            if arr_adverse[i] > hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, arr_adverse[i])

        res = [-n for n in hp]
        return res
