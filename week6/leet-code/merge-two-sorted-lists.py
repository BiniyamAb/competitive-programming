from async_timeout import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = merged = ListNode()
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    head.next = ListNode(list1.val)
                    head, list1 = head.next, list1.next
                else:
                    head.next = ListNode(list2.val)
                    head, list2 = head.next, list2.next
            elif list1:
                head.next = ListNode(list1.val)
                head, list1 = head.next, list1.next
            elif list2:
                head.next = ListNode(list2.val)
                head, list2 = head.next, list2.next
        
        return merged.next