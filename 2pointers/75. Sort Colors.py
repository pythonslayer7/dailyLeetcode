
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # use 3 pointers 

        left, mid, right = 0, 0, len(nums) - 1

        # left tracks the idx of the 0s
        # mid traverse thorugh the arr as the current idx of the current element
        # right is the bound and also tracks of the 2s

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
