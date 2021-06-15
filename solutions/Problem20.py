from helpers import Solution

from math import factorial


class SumOfDigitsOfFactorial(Solution):
    def __init__(self, n=100):
        self.N = n

    def _baby_solution(self):
        return sum(map(lambda y: int(y), str(factorial(self.N))))

    def solve(self):
        self._solve(chad=False)
