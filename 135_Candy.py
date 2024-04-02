# Exercise I:
# Mar 29, 2024
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1 for _ in range(len(ratings))]

        for i in range(1, len(candy)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1]+1

        for j in reversed(range(len(candy)-1)):
            if ratings[j] > ratings[j+1]:
                candy[j] = max(candy[j], candy[j+1]+1)

        return sum(candy)
