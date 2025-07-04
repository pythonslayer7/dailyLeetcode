from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        # dfs
        def dfs(node, currSum):
            if not node:
                return 0
            currSum = currSum * 10 + node.val

            # if it's a leaf node, return the currSum
            if not node.left and not node.right:
                return currSum
            
            # now we can find the sum of left node and right node
            return dfs(node.left, currSum) + dfs(node.right, currSum)
        return dfs(root, 0)
        