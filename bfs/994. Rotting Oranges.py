from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0)) # row, col, minute
                elif grid[i][j] == 1:
                    fresh += 1  
        
        # initiate directions 
        directions = [(-1,0),(1,0), (0, -1), (0, 1)]
        # edge case, no fresh orange, return 0 
        if fresh == 0:
            return 0
        while queue:
            (row, col, time) = queue.popleft()
            
            for dr, dc in directions:
                neighborRow, neighborCol = row + dr, col + dc
                if 0 <= neighborRow < rows and 0 <= neighborCol < cols and grid[neighborRow][neighborCol] == 1:
                    grid[neighborRow][neighborCol] = 2
                    queue.append((neighborRow, neighborCol, time + 1))
                    fresh -= 1
            
        return time if fresh == 0 else -1
