from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    from collections import deque
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(leftSubtree, rightSubtree):
            # base case if leftsubtree and rightsubtree are empty, must be mirror of itself
            if not leftSubtree and not rightSubtree:
                return True
            # base case if left or right subtree is missing, one is missing, then not mirror of itself
            if not leftSubtree or not rightSubtree:
                return False
            
            return (leftSubtree.val == rightSubtree.val and isMirror(leftSubtree.left, rightSubtree.right) and isMirror(leftSubtree.right, rightSubtree.left))
        
        # start comparing from the root
        return isMirror(root, root)