from typing import List
from collections import defaultdict
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # parent to child defaultdict
        tree = defaultdict(list)
        for child, parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(child)

        self.maxScore = 0
        self.count = 0 # how many nodes with highest score

        def dfs(node):
            size = 1 # current node has size 1 by itself
            score = 1 # multiplicative property 1 * something

            # traverse thorugh the children nodes
            for child in tree[node]:
                childSize = dfs(child)
                size += childSize
                score *= childSize
            
            # account for rest of the tree
            rest = len(parents) - size
            if rest > 0:
                score *= rest

            # find a maxScore, update it, and count 1 as in 1 node found with highest score
            if score > self.maxScore:
                self.maxScore = score
                self.count = 1
            # find other nodes with highest score later
            elif score == self.maxScore:
                self.count += 1

            return size
        
        dfs(0)
        return self.count # the total nodes with highest score

        # O(N) for time with traversing the N = len(parents) arr
        # O(N) for space with dfs the depth of the n levels and default dict space 