from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        que = [root]
        
        while que:
            temp = []
            vals = []
            for node in que:
                if node.left:
                    vals.append(node.left.val)
                    temp.append(node.left)
                else:
                    vals.append(None)
                if node.right:
                    temp.append(node.right)
                    vals.append(node.right.val)
                else:
                    vals.append(None)

            if vals != vals[::-1]:
                return False
            que = temp
        return True