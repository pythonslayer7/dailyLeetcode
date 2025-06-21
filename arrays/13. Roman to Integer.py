
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {"I": 1, "V": 5, "X": 10, "L":50, "C":100, "D": 500, "M": 1000 }
        total = 0
        for i in range(len(s) - 1):
            if symbol[s[i]] < symbol[s[i + 1]]:
                total -= symbol[s[i]] 
            else:
                total += symbol[s[i]]
            # add the last element
        total += symbol[s[-1]]
        return total
