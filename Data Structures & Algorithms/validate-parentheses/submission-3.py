class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        delta = [1, 2]

        for i in range(len(s)):

            if len(stack) != 0 and ord(s[i]) - stack[-1] in delta:
                stack = stack[:-1]
            else:
                stack.append(ord(s[i]))

        if stack:
            return False
        return True   