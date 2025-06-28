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
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # recurring case for left or right node, we find depth of 1 + left or right subtree
        return max(left, right) + 1
    # Time = O(N) N= num of nodes in the tree visited once
    # Space = O(h), h = height of the tree. Best case: O(logN) for balanced tree
    # worst case O(N) for skewed tree.

        # iterative way of solving it
        # queue = deque([(root, 1)])
        # maxDepth = 0
        # while queue:
        #   node, level = queue.popleft()
        #   maxDepth = max(maxDepth, level)
        # if node.left:
        #   queue.append(node.left, level + 1)
        #   queue.append(node.right, level + 1)
        # return maxDepth

        # Time = O(N)
        # Space = O(W), W = max number of nodes at any level
        # O(N) in the worst case, O (logn for balanced tree), O(1) for skwed tree 
            

