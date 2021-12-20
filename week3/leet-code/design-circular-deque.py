class MyCircularDeque:

    def __init__(self, k: int):
        self.dequ = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if len(self.dequ) == self.size:
            return False
        
        self.dequ.append(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.dequ) == self.size:
            return False
        
        self.dequ.insert(0, value)
        return True

    def deleteFront(self) -> bool:
        if not len(self.dequ) > 0:
            return False
        
        self.dequ.pop()
        return True
    
    def deleteLast(self) -> bool:
        if not len(self.dequ) > 0:
            return False
        
        self.dequ.remove(self.dequ[0])
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.dequ[-1]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.dequ[0]

    def isEmpty(self) -> bool:
        if len(self.dequ) > 0:
            return False
        return True
    
    def isFull(self) -> bool:
        if len(self.dequ) == self.size:
            return True
        return False