from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalIdx = len(nums) - 1

        # traverse the nums from the end
        for currIdx in reversed(range(len(nums))):
            # if overjump/exact jump to goalIdx, reassign goalIdx to currIdx
            if currIdx + nums[currIdx] >= goalIdx:
                goalIdx = currIdx
        return goalIdx == 0