class Node:
    def __init__(self):
        self.before = None
        self.value = None
        
class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = Node()

    def push(self, val: int) -> None:
        if len(self.stack) < 1:
            self.minn.value = val
        else:
            if val <= self.minn.value:
                temp = Node()
                temp.value = self.minn.value
                temp.before = self.minn.before
                self.minn.value = val
                self.minn.before = temp
                
        self.stack.append(val)
        
    def pop(self) -> None:
        if len(self.stack) < 2:
            pass
        elif self.minn.value == self.stack[-1]:
            self.minn = self.minn.before

        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]        
        
    def getMin(self) -> int:
        return self.minn.value