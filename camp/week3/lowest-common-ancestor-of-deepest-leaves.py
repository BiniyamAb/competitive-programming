from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def depth(self, root):
        if not root: return 0
        right = self.depth(root.right)
        left = self.depth(root.left)
        return max(right, left) + 1
        
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        right = self.depth(root.right)
        left = self.depth(root.left)
        if right == left:
            return root
        elif right > left:
            return self.lcaDeepestLeaves(root.right)
        else:
            return self.lcaDeepestLeaves(root.left)
        