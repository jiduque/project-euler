from math import sqrt

from helpers import Solution, timeit
from Problem7 import sieve_of_erasthenes


class MaxTotientFunction(Solution):
    def __init__(self, n=1000000):
        self.N = n

    def _chad_solution(self):
        bound = int(sqrt(self.N)) + 1
        list_of_primes = sieve_of_erasthenes(bound)[2:]  # returns 0 and 1 in list
        output = 1
        for prime in list_of_primes:
            if output * prime > self.N:
                break
            output *= prime

        return output

    def solve(self):
        self._solve(chad=True)
