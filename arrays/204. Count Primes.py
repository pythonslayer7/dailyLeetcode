class Solution:
    def countPrimes(self, n: int) -> int:
        # base case
        if n < 2:
            return 0
        isPrime = [True] * n # O(n) for time
        isPrime[0], isPrime[1] = False, False

        for i in range(2, int(n ** 0.5) + 1): # sqrt(n) for time
            if isPrime[i]:
                for j in range(i * i, n, i): # log
                    isPrime[j] = False
        return sum(isPrime)
    # O(N)loglog(N) for time
    # O(N) for space considering the isPrime arr

