from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        house1, house2 = 0, 0
        # 0, 0, 1, 2, 3
        # given [1, 2, 3]
        
        for num in nums:
            maxMoney = max(house1 + num, house2)
            house1 = house2
            house2 = maxMoney
        return maxMoney