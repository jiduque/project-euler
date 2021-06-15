from helpers import Solution

import numpy as np


class SumOfSpiralDiagonals(Solution):
    def __init__(self, n=1001):
        assert n % 2 == 1
        self.N = n

    def _baby_solution(self):
        i, total = 1, 1
        while 2 * i + 1 <= self.N:
            n = 2 * i + 1
            total += 4 * n ** 2 - 6 * (n - 1)
            i += 1
        return total

    def _chad_solution(self):
        coeffs = [-3/2, 4/3, 1/2, 2/3]
        return int(np.round(sum(map(lambda x: coeffs[x] * self.N ** x, range(4)))))

    def solve(self):
        self._solve(chad=True)
