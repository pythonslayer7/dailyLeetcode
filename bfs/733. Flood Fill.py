from collections import deque
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        startColor = image[sr][sc]
        queue = deque([(sr, sc)])

        if startColor == color:
            return image
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            row, col = queue.popleft()
            if image[row][col] == startColor:
                image[row][col] = color
            for dr, dc in directions:
                neighborRow, neighborCol = row + dr, col + dc
                if 0 <= neighborRow < rows and 0 <= neighborCol < cols and image[neighborRow][neighborCol] == startColor:
                    queue.append((neighborRow, neighborCol))
        return image