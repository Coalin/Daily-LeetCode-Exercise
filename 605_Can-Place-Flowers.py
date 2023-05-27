# Exercise I:
# May 27, 2023

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = 0

        if len(flowerbed) == 1:
            if flowerbed == [0]:
                return n <= 1
            elif flowerbed == [1]:
                return n <= 0

        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[1] == 0:
                    total += 1
                    flowerbed[0] = 1
            if i > 0 and i < len(flowerbed)-1:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    total += 1
                    flowerbed[i] = 1
            if i == len(flowerbed)-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    total += 1
                    flowerbed[i] = 1
        
        return total >= n
