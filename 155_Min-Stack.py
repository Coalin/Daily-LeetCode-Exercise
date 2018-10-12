class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            pre_min = 2**32-1
        else:
            pre_min = self.stack[-1][1]
        self.stack.append([x, min(x, pre_min)])
        

    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
