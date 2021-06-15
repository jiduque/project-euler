from helpers import Solution
from math import sqrt, log


class SumOfEvenFibonacciBelow(Solution):
    def __init__(self, n=4000000):
        self.N = n
        self.sqrt5 = sqrt(5)
        self.phi3 = ((1 + self.sqrt5) / 2) ** 3
        self.psi3 = ((1 - self.sqrt5) / 2) ** 3

    def _kth_even_fib(self, k):
        coeffs = (1, -1)
        terms = map(lambda x: x ** k, [self.phi3, self.psi3])
        return int(sum(map(lambda x: x[0] * x[1], zip(coeffs, terms))) / self.sqrt5)

    def _find_bound(self):
        output = int(log(self.sqrt5 * self.N) / log(self.phi3))

        while self._kth_even_fib(output + 1) < self.N:
            output += 1

        return output

    def _baby_solution(self):
        output = 0
        fib_k, fib_k1 = 1, 1
        fib_k2 = fib_k + fib_k1
        while fib_k2 < self.N:
            if fib_k2 % 2 == 0:
                output += fib_k2
            fib_k = fib_k1
            fib_k1 = fib_k2
            fib_k2 = fib_k + fib_k1

        return output

    def _chad_solution(self):
        coeffs = (1, -1)
        bound = self._find_bound()
        terms = map(lambda x: (1 - x**(bound + 1)) / (1 - x), [self.phi3, self.psi3])
        return int(sum(map(lambda x: x[0] * x[1], zip(coeffs, terms))) / self.sqrt5)

    def solve(self):
        self._solve(chad=False)
