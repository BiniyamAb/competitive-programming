from async_timeout import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        f, s = head, head
        
        for _ in range(n): f = f.next
        while f and f.next: s, f = s.next, f.next
        if f == None: return s.next
        s.next = s.next.next
        
        return head