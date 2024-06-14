"""
    Whether you make the expensive operation the push or the pop depends on your use
    case. Aparently for leetcode's purposes it is better to make pop the expensive operation
"""
class MyQueue:
    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.aux.append(self.stack.pop())
        element = self.aux.pop()
        while self.aux:
            self.stack.append(self.aux.pop())
        return element

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
