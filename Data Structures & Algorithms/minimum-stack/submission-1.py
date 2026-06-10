class MinStack:

    def __init__(self):

        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:

        if not self.stack:
            self.minimum.append(val)
        else:
            if self.minimum[-1] >= val:
                self.minimum.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        
        last = self.stack.pop()

        if last == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:

        return self.stack[-1]

    def getMin(self) -> int:

        return self.minimum[-1]