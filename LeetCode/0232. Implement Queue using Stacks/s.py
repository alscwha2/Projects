class MyQueue:
    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, x: int) -> None:
        while self.stack:
            self.aux.append(self.stack.pop())
        self.stack.append(x)
        while self.aux:
            self.stack.append(self.aux.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
