from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time = O(log(mxn))
        # Space = O(1)
        left, right = 0, len(matrix[0]) * len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            currentVal = matrix[row][col]

            if currentVal < target:
                left = mid + 1
            elif currentVal > target:
                right = mid - 1
            else:
                return True
        return False
