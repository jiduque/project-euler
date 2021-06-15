from helpers import Solution

from math import factorial


class LatticePaths(Solution):
    def __init__(self, n=20):
        super().__init__(n)

    def _chad_solution(self):
        return factorial(2*self.N) // (factorial(self.N)**2)

    def solve(self):
        self._solve(chad=True)
