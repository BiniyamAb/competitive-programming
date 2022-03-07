class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root, parent, grandParent):
        if not root: return
        if grandParent and grandParent%2 == 0:
            self.summ += root.val
        self.dfs(root.right, root, parent.val)
        self.dfs(root.left, root, parent.val)
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.summ = 0
        if not root.right and not root.left: return 0
        self.dfs(root.right, root, None)
        self.dfs(root.left, root, None)
        return self.summ