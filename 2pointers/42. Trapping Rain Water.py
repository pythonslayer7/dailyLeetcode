from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = 0, 0
        # two pointers to trap water, move the shorter bar
        left, right = 0, len(height) - 1
        trap = 0
        while left < right:
            if height[left] < height[right]:
                maxLeft = max(maxLeft, height[left])
                trap += max(0, maxLeft - height[left])
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                trap += max(0, maxRight - height[right])
                right -= 1
        return trap 
