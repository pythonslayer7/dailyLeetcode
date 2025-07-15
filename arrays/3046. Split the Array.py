from typing import List
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        num1Set = set()
        num2Set = set()

        for num in nums:
            if num not in num1Set:
                num1Set.add(num)
            elif num not in num2Set:
                num2Set.add(num)
            else:
                return False
        return True

        