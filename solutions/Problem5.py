from helpers import Solution
from functools import reduce


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


class LCMBelow(Solution):
    def __init__(self, n=20):
        self.N = n

    def _baby_solution(self):
        upper_bound = reduce(lambda x, y: x*y, range(2, self.N+1))
        for i in range(1, upper_bound):
            if all(i % j == 0 for j in range(2, self.N+1)):
                return i
        return upper_bound

    def _chad_solution(self):
        return reduce(lcm, range(2, self.N+1))

    def solve(self):
        self._solve(chad=True)
