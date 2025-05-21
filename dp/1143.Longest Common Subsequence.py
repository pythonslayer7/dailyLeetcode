class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # initialize 2d table to 0, with extra row and col to accound for empty strings for text1 and text2. 0 because empty strings are 0 len matching
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]