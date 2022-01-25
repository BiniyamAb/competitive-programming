from ast import List
from async_timeout import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack, arr, ind = [], [], 0
        while head:
            arr.append(0)
            while stack and stack[-1][0] < head.val:
                arr[stack[-1][1]] = head.val
                stack.pop()
            stack.append([head.val, ind])
            head = head.next
            ind+=1
        
        return arr