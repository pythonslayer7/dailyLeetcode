from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case, root is empty or none, return False
        if not root:
            return False
        # base case, we have a leaf node with no children, we check if targetSum == root val
        if not root.left and not root.right:
            return targetSum == root.val
        # get new remaining sum and recurse on the left and right subtrees
        remaining = targetSum - root.val 
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
