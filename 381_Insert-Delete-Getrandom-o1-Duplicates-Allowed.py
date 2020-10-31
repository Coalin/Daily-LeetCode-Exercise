import random
import math

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.idx = dict()
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val in self.idx:
            flag = False
            self.idx[val].append(len(self.nums))
        else:
            flag = True
            self.idx[val] = [len(self.nums)]
        self.nums.append(val)
        return flag  


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.idx:
            if len(self.idx[val]): 
                flag = True
                if self.nums[-1] == val:
                    self.idx[val].remove(len(self.nums)-1)
                    self.nums.pop()
                else:
                    self.idx[self.nums[-1]].remove(len(self.nums)-1)
                    self.idx[self.nums[-1]].append(self.idx[val][-1])
                    self.nums[self.idx[val][-1]] = self.nums[-1]
                    self.idx[val].remove(self.idx[val][-1])
                    self.nums.pop()
            else:
                flag = False 
        else:
            flag = False

        return flag


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        rnd = math.floor(random.random()*len(self.nums))
        return self.nums[rnd]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
