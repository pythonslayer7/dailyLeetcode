from typing import List
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize color arr with all 0s
        colors = [0] * n
        result = []
        count = 0

        for index, newColor in queries:
            oldColor = colors[index]
            # check left bounds, if it's oldColor and != 0, if same color, decrement count
            if index > 0 and colors[index - 1] == oldColor and oldColor != 0:
                count -= 1
            # check right bounds, if it's oldColor and != 0, if same color, decrement coung
            if index < n - 1 and oldColor == colors[index + 1] and oldColor != 0:
                count -= 1
            # update new color
            colors[index] = newColor

            if index > 0 and colors[index - 1] == newColor and newColor != 0:
                count += 1
            
            if index < n - 1 and colors[index + 1] == newColor and newColor != 0:
                count += 1
            result.append(count)
        return result
