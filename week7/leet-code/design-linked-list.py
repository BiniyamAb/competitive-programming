class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class MyLinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:             
        count = 0
        llist = self.head
        while llist:
            if count == index:
                return llist.val
            llist = llist.next
            count+=1
        return -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        temp = self.head
        self.head = Node(val)
        self.head.next = temp

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        llist = self.head
        while llist.next:
            llist = llist.next
        llist.next = Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            if not self.head:
                self.head = Node(val)
                return
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
            return
        llist = self.head
        count = 0
        while llist:
            if count+1 == index:
                new = Node(val)
                new.next = llist.next
                llist.next = new
                return
            llist = llist.next
            count+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if not self.head:
                return
            self.head = self.head.next
            return
        llist = self.head
        count = 0
        while llist:
            if llist.next and count+1 == index:
                llist.next = llist.next.next
                return
            llist = llist.next
            count+=1
