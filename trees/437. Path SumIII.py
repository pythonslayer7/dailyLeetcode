from typing import Optional
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = []
        prefixSumFreq = defaultdict(int) # prefixSum to freq
        prefixSumFreq[0] = 1 # with sum to 0, only 1 way since prefixSumFreq[currSum - targetSum] == prefixSumFreq[0]= 1
        def dfs(node, currSum):
            if not node:
                return 0

            currSum += node.val
            # find how many earlier paths had a sum so that the current path sums to target
            pathEndHere = prefixSumFreq[currSum - targetSum]

            # record currSum for child nodes to use
            prefixSumFreq[currSum] += 1

            # recurse on left and right subtree
            pathEndHere += dfs(node.left, currSum)
            pathEndHere += dfs(node.right, currSum)

            # remove currSum so it doesnt affect sibling subtrees
            prefixSumFreq[currSum] -= 1
            return pathEndHere
        return dfs(root, 0)