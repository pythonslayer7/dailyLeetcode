from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # edge case, if starting cell or ending cell is not 0, then return -1
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        # initiate visited arr to False. set the starting cell as True
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        # add the top-left cell to a queue
        queue = deque([(0, 0, 1)]) # row, col, currLen
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        while queue:
            # popleft
            row, col, currLen = queue.popleft()
            # base case if we're at end of row and col, return currLen
            if row == n - 1 and col == n - 1:
                return currLen
            # traverse through directions
            for dr, dc in directions:
                neighborRow, neighborCol = dr + row, dc + col
                # check bounds, check if grid cell is 0 and not visited
                if (0 <= neighborRow < n and 0 <= neighborCol < n and
                     grid[neighborRow][neighborCol] == 0 and not visited[neighborRow][neighborCol]):
                    visited[neighborRow][neighborCol] = True
                    queue.append((neighborRow, neighborCol, currLen + 1))
               
            return -1   
                    
