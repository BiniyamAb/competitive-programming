from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left) if root.left else 0
        right = self.dfs(root.right) if root.right else 0
        self.tilts += abs(left - right)
        return left + right + root.val
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilts = 0
        self.dfs(root)
        return self.tilts