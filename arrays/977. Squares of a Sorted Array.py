from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * (len(nums))
        # fill from the end
        currPos = len(nums) - 1
        # two pointer
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                result[currPos] = nums[right] ** 2
                right -= 1
            else:
                result[currPos] = nums[left] ** 2
                left += 1
            currPos -= 1
        return result
    # O(n) time, O(1) space
