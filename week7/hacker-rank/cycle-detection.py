def has_cycle(head):
    if not head:
        return 0
    set1 = set()
    while head:
        if head in set1:
            return 1
        set1.add(head)
        head = head.next
    return 0