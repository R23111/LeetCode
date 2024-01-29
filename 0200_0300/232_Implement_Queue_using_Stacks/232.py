class MyQueue:
    def __init__(self):
        self.entities = []

    def push(self, x: int) -> None:
        self.entities.append(x)

    def pop(self) -> int:
        value = self.entities[0]
        for i in range(len(self.entities) - 1):
            self.entities[i] = self.entities[i + 1]
        self.entities = self.entities[:-1]
        return value

    def peek(self) -> int:
        return self.entities[0]

    def empty(self) -> bool:
        return not bool(self.entities)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
