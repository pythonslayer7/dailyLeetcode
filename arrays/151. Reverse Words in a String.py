class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        return " ".join(wordList[::-1])
        