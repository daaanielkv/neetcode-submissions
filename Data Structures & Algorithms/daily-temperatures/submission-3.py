class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        res = []
        stack = []

        for i in range(len(temperatures) - 1):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = (i - stack[-1])
                stack.pop()
            if temperatures[i] >= temperatures[i + 1]:
                res.append(0)
                stack.append(i)      
            else:
                res.append(1)  
        while stack and temperatures[stack[-1]] < temperatures[-1]:
            res[stack[-1]] = (len(temperatures) - 1 - stack[-1])
            stack.pop()
        res.append(0)
        return res