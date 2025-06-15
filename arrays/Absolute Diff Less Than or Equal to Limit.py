from typing import List
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeq = deque()
        minDeq = deque()
        left = 0
        maxLen = 0
        resWindow = 0

        for right in range(len(nums)):
            # Maintain the maxDeq
            while maxDeq and nums[maxDeq[-1]] <= nums[right]:
                maxDeq.pop()
            maxDeq.append(right)

            while minDeq and nums[minDeq[-1]] >= nums[right]:
                minDeq.pop()
            minDeq.append(right)

            # If window is invalid, pop fro
            while nums[maxDeq[0]] - nums[minDeq[0]] > limit:
                if maxDeq[0] == left:
                    maxDeq.popleft()
                if minDeq[0] == left:
                    minDeq.popleft()    
                left += 1
            resWindow = max(resWindow, right - left + 1)
        return resWindow
