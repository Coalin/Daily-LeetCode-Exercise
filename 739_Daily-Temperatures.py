class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Solution 1:
        # 超出时间限制
        # res = [0 for _ in range(len(temperatures))]

        # for i in range(len(temperatures)-1):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j-i 
        #             break 
        
        # return res
                

        # Solution 2:
        # 增加break条件
        # 超出时间限制
        # 再优化,第二个循环每步步长拉长至res[j],AC
        # res = [0 for _ in range(len(temperatures))]

        # for i in reversed(range(len(temperatures)-1)):
        #     # for j in range(i+1, len(temperatures)):
        #     j = i+1 
        #     while j < len(temperatures):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j-i 
        #             break 
        #         elif res[j] == 0:
        #                 break 
        #         j += res[j]
        
        # return res
                
        # Solution 3:
        # 单调栈解法
        res = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                    res[stack[-1]] = i-stack[-1]
                    stack.pop()
            stack.append(i)

        return res
