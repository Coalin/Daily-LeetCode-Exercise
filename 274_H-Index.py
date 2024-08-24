# Exercise I:
# Aug 23, 2024
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0 
        citations_reverse_sorted = sorted(citations)[::-1]
        print(citations_reverse_sorted)

        for i in range(len(citations_reverse_sorted)):
            if citations_reverse_sorted[i] < i+1:
                break 
            h_index = i+1 

        return h_index
