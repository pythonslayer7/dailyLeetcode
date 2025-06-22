from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search with O(log n)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # check if left half is sorted
            if nums[left] <= nums[mid]:
                # target is within the left, smaller than the nums[mid] 
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # target is in the left half, so we shift right pointer to the left
                else:
                    left = mid + 1
            else:
                # in the right is sorted
                # target <= nums[right], but greater than nums[mid]
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 