from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # traverse from the end
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits # increment by 1 and return immediately
            else:
                digits[i] = 0

        # all digits are 9s [9, 9, 9]
        return [1] + digits
      
      # Time O(N) Space O(1)