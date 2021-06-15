from helpers import Solution

from Problem7 import sieve_of_erasthenes


class SumOfPrimesBelow(Solution):
    def __init__(self, n=2000000):
        self.N = n

    def _baby_solution(self):
        return sum(sieve_of_erasthenes(self.N-1)) - 1

    def solve(self):
        self._solve(chad=False)
