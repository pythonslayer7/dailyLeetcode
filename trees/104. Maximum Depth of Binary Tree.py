from typing import Optional

# Definition for a binary tree node
class TreeNode:
   def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case or end of node, depth is 0
        if not root:
            return 0
        # recurring case for left or right node, we find depth of 1 + left or right subtree
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            

