from typing import List
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxDistance = 0

        for i in range(len(colors)):
            # compare with the first house
            if colors[i] != colors[0]:
                maxDistance = max(maxDistance, i)

            # compare with the last house
            if colors[i] != colors[-1]:
                maxDistance = max(maxDistance, len(colors) - i - 1)
        return maxDistance