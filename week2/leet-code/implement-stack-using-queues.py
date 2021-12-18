class MyStack:

    def __init__(self):
        self.stack = []        

    def push(self, x: int) -> None:
        self.stack.insert(0, x)
        for i in range(len(self.stack) - 1):
            num = self.stack.pop()
            self.stack.insert(0, num)
            
    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not bool(self.stack)