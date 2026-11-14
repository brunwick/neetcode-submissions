class MinStack:

    def __init__(self):
        self.stack, self.mins = [], []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mins.append(min(val, self.mins[-1]) if self.mins else val)

    def pop(self) -> None:
        top = self.stack[-1]
        del self.stack[-1]
        del self.mins[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
