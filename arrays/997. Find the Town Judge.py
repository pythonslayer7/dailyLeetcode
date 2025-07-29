from collections import defaultdict
from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustscore = defaultdict(int)
        for p1, p2 in trust:
            trustscore[p1] -= 1 # p1 trusts p2, so p1 lose a score
            trustscore[p2] += 1 # p2 is trusted by p1, so add a score

        for person in range(1, n + 1):
            if trustscore[person] == n - 1: # judge trusts no one, but everyone except the judge trusts the judge
                return person
        return -1
        