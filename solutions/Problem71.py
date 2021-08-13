from helpers import Solution
from Problem5 import gcd


class LargestProperFractionWithDenominatorLessThan(Solution):
    def __init__(self, n=1000000, a=3, b=7):
        self.N = n
        self.a = a
        self.b = b

    def _chad_solution(self):
        d = self.N
        c = (self.a * d - 1) // self.b

        while self.a * d - self.b * c != 1:
            d -= 1
            c = (self.a * d - 1) // self.b

        hcf = gcd(c, d)
        c //= hcf
        d //= hcf

        return c, d

    def solve(self):
        self._solve(chad=True)
