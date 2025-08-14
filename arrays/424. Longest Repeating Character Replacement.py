from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counterDict = defaultdict(int)
        left = 0
        maxFreq = 0
        longestLen = 0
        for right, char in enumerate(s):
            counterDict[char] += 1
            maxFreq = max(maxFreq, counterDict[char])

            #narrow the window
            while (right - left + 1) - maxFreq > k:
                counterDict[s[left]] -= 1 # decrement the one leaving the window
                left += 1
            longestLen = max(right - left + 1, longestLen)

        return longestLen