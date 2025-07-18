class Solution:
    def climbStairs(self, n: int) -> int:
        # base case
        if n <= 2:
            return n

        # to reach step1, only 1 way [[1]]
        # to reach step2, 2 ways [[2], [1, 1]]
        step1Way, step2Way = 1, 2

        # start with step 3, to step n inclusive
        for _ in range(3, n + 1):
            totalWay = step1Way + step2Way
            step1Way = step2Way
            step2Way = totalWay
        return step2Way