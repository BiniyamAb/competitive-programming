class MyQueue:
    
    def __init__(self):
        self.lst = []
        
    def push(self, x: int) -> None:
        self.lst.insert(0, x)      

    def pop(self) -> int:
        return self.lst.pop()
    
    def peek(self) -> int:
        return self.lst[-1]

    def empty(self) -> bool:
        if self.lst:
            return False
        else:
            return True