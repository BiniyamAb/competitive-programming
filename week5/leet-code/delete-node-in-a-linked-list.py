class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        head = node
        while(head.next):
            head.val = head.next.val
            if head.next.next == None:
                break
            head = head.next
        head.next = None
        return