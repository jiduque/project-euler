from helpers import Solution, timeit

from Problem5 import gcd
from math import sqrt


class SpecialPythagoreanTriplet(Solution):
    def __init__(self, n=1000):
        self.N = n

    def _baby_solution(self):
        for a in range(1, self.N // 3 + 1):
            for b in range(a, self.N // 2 + 1):
                c = self.N - a - b
                if c ** 2 == (a ** 2) + (b ** 2):
                    return a * b * c
        return None

    def _chad_solution(self):
        half_n = self.N // 2
        bound = int(sqrt(half_n))
        for m in range(2, bound + 1):
            if half_n % m == 0:
                lwr_bnd = m + 2
                if m % 2 == 0:
                    lwr_bnd -= 1
                x = half_n // m
                upr_bnd = min(2 * m, x + 1)
                for k in range(lwr_bnd, upr_bnd, 2):
                    if x % k == 0 and gcd(k, m) == 1:
                        d = x // k
                        n = k - m
                        a = d * (m**2 - n**2)
                        b = 2 * d * n * m
                        c = d * (m**2 + n**2)
                        return a * b * c
        return None

    def solve(self):
        self._solve(chad=True)
