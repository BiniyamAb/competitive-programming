class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        lst = []
        if root.children:
            for i in range(len(root.children)):
                lst.append(self.maxDepth(root.children[i]))
        if not lst:
            return 1
        return max(lst) + 1