# Exercise I:
# July 8, 2023

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions = sorted(potions)

        for i in spells:
            l = 0 
            r = len(potions)-1 

            # r is the last number not to meet the demand
            while l <= r:
                m = (r-l)//2+l 
                if potions[m]*i >= success:
                    r = m-1 
                else:
                    l = m+1 
                        
            res.append(len(potions)-r-1)

        return res         
