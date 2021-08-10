from math import log

from helpers import Solution
from Problem3 import LargestPrimeFactorOf


def sieve_of_erasthenes(bound):
    prime = [[i, True] for i in range(bound + 1)]
    p = 2
    while p * p <= bound:
        if prime[p][1]:
            for i in range(p * p, bound + 1, p):
                prime[i][1] = False
        p += 1
    return list(map(lambda x: x[0], filter(lambda x: x[1], prime)))


class NthPrime(Solution):
    def __init__(self, n=10001):
        self.N = n

    def _estimate_bound(self):
        return int(self.N * (log(self.N) + log(log(self.N)))) + 1

    def _baby_solution(self):
        if self.N == 1:
            return 2
        prime_counter, num = 2, 3
        while prime_counter != self.N:
            num += 2
            lpf = LargestPrimeFactorOf(num)._chad_solution()
            if lpf == num:
                prime_counter += 1

        return num

    def _chad_solution(self):
        if self.N < 17:
            return self._baby_solution()
        upper_bound = self._estimate_bound()
        list_of_primes = self._sieve_of_erasthenes(upper_bound)
        return list_of_primes[self.N+1]

    def solve(self):
        self._solve(chad=True)
