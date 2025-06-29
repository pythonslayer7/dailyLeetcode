from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case, if node is empty
        if not root:
            return None 
        
        # recursive with postorder logic, we swap the left and righ node 
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root