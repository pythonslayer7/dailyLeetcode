from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for idx, value in enumerate(nums): # value to idx
            
            if target - value in hashMap:
                return [idx, hashMap[target - value]]
            hashMap[value] = idx
        return 
            