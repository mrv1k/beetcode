# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            prev_min = self.min_stack[-1]
            self.min_stack.append(min(prev_min, val))
        # cleaner way to write would be
        # prev_min = min(val, self.min_stack[-1] if self.min_stack else val)
        # self.min_stack.append(min(prev_min, val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        x = self.stack[-1]
        print(x)
        return x

    def getMin(self) -> int:
        x = self.min_stack[-1]
        print(x)
        return x


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# [null, null, null, null, -3, null, 0, -2]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()  # return -3
minStack.pop()
minStack.top()  # return 0
minStack.getMin()  # return -2
