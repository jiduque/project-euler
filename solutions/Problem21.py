from helpers import Solution

from math import sqrt, ceil


def sum_divisors(number):
    upper_bound = ceil(sqrt(number))
    output = 0
    for i in range(1, upper_bound + 1):
        a, b = divmod(number, i)
        if b == 0:
            output += i + a
    return output - number


class SumAmicableNumbers(Solution):
    def __init__(self, n=10000):
        self.N = n

    def _baby_solution(self):
        output = 0
        for a in range(1, self.N + 1):
            b = sum_divisors(a)
            if (b > a) and (sum_divisors(b) == a):
                output += a + b
        return output

    def solve(self):
        self._solve(chad=False)
