from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two pointers at the end of actual values of nums1 and nums2, mergepointer at last idx of nums1
        nums1Idx, nums2Idx, mergeIdx = m - 1, n - 1, len(nums1) - 1

        while nums1Idx >= 0 and nums2Idx >= 0:
            # compare the last elements of num1 and num2 arr, reset
            # the last ele of num1 to the bigger val, increment idx
            if nums1[nums1Idx] > nums2[nums2Idx]:
                nums1[mergeIdx] = nums1[nums1Idx]
                nums1Idx -= 1
            else:
                nums1[mergeIdx] = nums2[nums2Idx]
                nums2Idx -= 1
            mergeIdx -= 1

        # edge cases
        while nums2Idx >= 0:
            nums1[mergeIdx] = nums2[nums2Idx]
            mergeIdx -= 1
            nums2Idx -= 1