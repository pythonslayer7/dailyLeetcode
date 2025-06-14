from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def bfs(currRow, currCol):
            queue = deque([(currRow, currCol)]) # row, col
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while queue:
                currRow, currCol = queue.popleft()
                for dr, dc in directions:
                    neiRow, neiCol = currRow + dr, currCol + dc
                    if(0 <= neiRow < rows and 0 <= neiCol < cols and grid[neiRow][neiCol] == "1" and not visited[neiRow][neiCol]):
                        visited[neiRow][neiCol] = True
                        queue.append((neiRow, neiCol))
        island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    island += 1
        return island
    # Time O(m x n) traverse the grid to find 1s, ignore 0s
    # Space O(m x n) visited matrix (m x n) and queue the worse case = O(m x n) if all land cells 1s. 
