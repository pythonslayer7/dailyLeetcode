from typing import List
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        centerCell = len(grid) // 2
        minChange = n * n
        # run through all combinations of possible yNum and bgNum, and skip if they're the same.
        for yNum in range(3):
            for bgNum in range(3):
                if yNum == bgNum:
                    continue
                
                change = 0
                # traverse through the grid
                for row in range(n):
                    for col in range(n):
                        # check if curr cell is diagonal or vertical to ensure that it's y shaped and in bounds
                        diagonal = ((row == col or row + col == n - 1) and row <= centerCell)
                        vertical = row >= centerCell and col == centerCell 
                        # (0, 0), (0, 1), (0, 2)
                        # (1, 0), (1, 1), (1, 2)
                        # (2, 0), (2, 1), (2, 2)
                        yShape = diagonal or vertical
                        if yShape:
                            if grid[row][col] != yNum:
                                change += 1
                        else:
                            if grid[row][col] != bgNum:
                                change += 1
                minChange = min(change, minChange)
        return minChange