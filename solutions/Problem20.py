from helpers import Solution

from math import factorial


class SumOfDigitsOfFactorial(Solution):
    def __init__(self, n=10):
        super().__init__(n)

    def _baby_solution(self):
        return sum(map(lambda y: int(y), str(factorial(self.N))))

    def solve(self):
        self._solve(chad=False)
