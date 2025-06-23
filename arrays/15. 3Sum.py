from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, value in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            
            while left < right:
                threeSum = nums[index] + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    result.append([value, nums[left], nums[right]])
                    left += 1
                    # eliminate duplicates in triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
        return result
