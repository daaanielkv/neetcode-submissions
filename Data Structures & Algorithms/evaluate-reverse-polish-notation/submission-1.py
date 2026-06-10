class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        tasks = {'+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: int(x / y)}
        
        res = []

        for elem in tokens:
            if elem in tasks:
                res[-2] = tasks[elem](res[-2], res[-1])
                res.pop()
            else:
                res.append(int(elem))

        return res[0]