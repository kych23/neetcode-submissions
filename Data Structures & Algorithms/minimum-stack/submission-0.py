# Have a normal stack, but keep track of the current minimum element at this operation
# - elements be (value, min_value)
# - if stack empty, we append (value, value)
# - if stack not empty, we append (value, min(stack[-1][1], value))
# - pop will return first index, getMin will return second index

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            minimum = min(self.stack[-1][1], val)
            self.stack.append((val, minimum))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
