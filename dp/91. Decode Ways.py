class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        TwoWaysBack = 1
        OneWaysBack = 1

        for i in range(1, len(s)):
            currentWay = 0
            if s[i] != "0":
                currentWay += OneWaysBack
            
            # check two chars back
            twoChars = int(s[i-1:i+1])
            if 10 <= twoChars <= 26:
                currentWay += TwoWaysBack
            
            TwoWaysBack, OneWaysBack = OneWaysBack, currentWay
        return OneWaysBack
        