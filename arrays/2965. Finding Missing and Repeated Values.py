from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        distinct = set()
        result = []
        n = len(grid)
        # look for repeated value
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] in distinct:
                    result.append(grid[row][col])
                distinct.add(grid[row][col])

        # look for missing value
        for i in range(1, n * n + 1):
            if i not in distinct:
                result.append(i)
        return result 

        # time = O(N^2) space = O(N^2)