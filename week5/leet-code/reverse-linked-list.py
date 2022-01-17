from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        reverse = ListNode(head.val)
        head = head.next
        while(head!=None):
            temp = reverse
            reverse = ListNode(head.val)
            reverse.next = temp
            head = head.next
        
        return reverse