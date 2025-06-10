from collections import deque
from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadSet = set(deadends)
        visited = set()
        start = "0000"
        queue = deque([(start, 0)]) # currComb, step
        visited.add(start)
        # edge case
        if start in deadSet:
            return -1
        
        while queue:
            currComb, step = queue.popleft()
            # base case
            if currComb == target:
                return step
            # traverse thorugh 4 locks:
            for i in range(4):    
                for move in [-1, 1]: # going up or down for every 4 lock
                    numsList = list(currComb)
                    newNum = (int(numsList[i]) + move + 10) % 10 # keep newNum in 0-9
                    numsList[i] = str(newNum)
                    newComb = "".join(numsList)
                    if newComb not in visited and newComb not in deadSet:
                        visited.add(newComb)
                        queue.append((newComb, step + 1))
        return -1 