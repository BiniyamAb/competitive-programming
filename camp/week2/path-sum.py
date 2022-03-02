from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root, summ):
        if not root.left and not root.right:
            self.sums.add(summ + root.val)
            return
        if root.left:
            self.dfs(root.left, summ + root.val)
        if root.right:
            self.dfs(root.right, summ + root.val)
            
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        self.sums = set()
        self.dfs(root, 0)
        return targetSum in self.sums