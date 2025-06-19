class Solution:
    def isHappy(self, n: int) -> bool:
        mySet = set()
        def findSumSquares(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n = n // 10
            return total

        while n != 1:
            if n in mySet:
                return False
            else:
                mySet.add(n)
                n = findSumSquares(n)
        return True
#Time	O(log n) per step × constant steps → practically O(1) for math
#Space	O(1) → the set only holds a small number of values (< 243)