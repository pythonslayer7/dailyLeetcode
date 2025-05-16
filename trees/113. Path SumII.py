from typing import Optional, List
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node, currComb, remaining):
            # base case
            if not node:
                return
            
            # add node.val to current comb
            currComb.append(node.val)
            
            # leaf node with no children, end of node and reached targetSum
            if not node.left and not node.right and node.val == remaining:
                result.append(currComb[:])

            remaining = remaining - node.val
            dfs(node.left, currComb, remaining)
            dfs(node.right, currComb, remaining)
            currComb.pop()
        
        dfs(root, [], targetSum)
        return result

                


