from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(currPerm, isUsed):
            # base case, found a permutation
            if len(currPerm) == len(nums):
                result.append(currPerm[:])
            
            for i in range(len(nums)):
                if not isUsed[i]:
                    currPerm.append(nums[i])
                    isUsed[i] = True
                    dfs(currPerm, isUsed)
                    currPerm.pop()
                    isUsed[i] = False

        isUsed = [False] * len(nums)
        dfs([], isUsed)
        return result


