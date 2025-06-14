from collections import defaultdict
from typing import List
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # goal is to count how many 2x2 blocks have 0 - 4 black cells
        # block_counts only stores blocks that are touched by at least one black cell, we will have to find 0 black cell later
        blockCounts = defaultdict(int)
        # Key: coordinates of the top-left cell of a 2x2 block (i.e., a tuple (i, j))
        # Value: how many black cells are inside that 2x2 block
        #These 4 direction offsets represent the top-left corner of every 2x2 block that a black cell (x, y) could belong to.
        directions = [(0, 0), (-1, 0), (0, -1), (-1, -1)]
        for x, y in coordinates:
            for dx, dy in directions:
                blockRow, blockCol = x + dx, y + dy
                if 0 <= blockRow < m - 1 and 0 <= blockCol < n - 1:
                    blockCounts[(blockRow, blockCol)] += 1
        
        result = [0] * 5
        for count in blockCounts.values():
            result[count] += 1
        
        # look for 0 count of 2x2 blocks for black blocks
        totalBlocks = (m - 1) * (n - 1)
        result[0] = totalBlocks - sum(result[1:])
        return result
