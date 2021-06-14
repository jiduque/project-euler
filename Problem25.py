from helpers import Solution

from math import log, sqrt


class NDigitFibonacciNumber(Solution):
    def __init__(self, n=3):
        super().__init__(n)
        self.sqrt5 = sqrt(5)
        self.phi = (1 + self.sqrt5) / 2
        self.digit_bound = 10 ** (self.N-1)
        self.fibo_dict = {1: 1, 2: 1}

    def _kth_fibonacci(self, k):
        if k not in self.fibo_dict:
            i = 1
            while k not in self.fibo_dict:
                self.fibo_dict[i+2] = self.fibo_dict[i+1] + self.fibo_dict[i]
                i += 1

        return self.fibo_dict[k]

    def _find_bound(self):
        return int((log(self.sqrt5) + (self.N - 1) * log(10)) / log(self.phi))

    def _chad_solution(self):
        k = self._find_bound()
        while self._kth_fibonacci(k) < self.digit_bound:
            k += 1
        return k

    def solve(self):
        self._solve(chad=True)
