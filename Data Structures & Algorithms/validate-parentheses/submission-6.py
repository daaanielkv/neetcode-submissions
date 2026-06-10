class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        matching = {')': '(', 
                    ']': '[', 
                    '}': '{'}

        for elem in s:
            if elem in matching:
                if not stack or stack[-1] != matching[elem]:
                    return False
                stack.pop()
            else:
                stack.append(elem)
        
        return not stack