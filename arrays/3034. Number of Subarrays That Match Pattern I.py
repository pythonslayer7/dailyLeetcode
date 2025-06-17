from typing import List
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        # make delta arr to find diff in nums arr
        delta = []
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                delta.append(-1)
            elif nums[i] < nums[i + 1]:
                delta.append(1)
            else:
                delta.append(0)
        # look for the subarr of pattern in delta arr
        count = 0
        
        for i in range(len(delta) - len(pattern) + 1):
            match = False # initiate to false at beginning of each loop    
            for j in range(len(pattern)):
                if delta[i+j] != pattern[j]:
                    match = False
                    break
                else:
                    match = True
            if match:
                count += 1
        return count
