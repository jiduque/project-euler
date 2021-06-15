from helpers import Solution

from math import sqrt


def triangular_number(x):
    return x * (x + 1) // 2


def num_divisors(x):
    upper_bound = int(sqrt(x)) + 1
    return 2 * sum(map(lambda num: x % num == 0, range(1, upper_bound)))


class FirstTriangularNumberWithOverNDivisors(Solution):
    def __init__(self, n=500):
        self.N = n

    def _baby_solution(self):
        i = 1
        curr_val = triangular_number(i)

        while num_divisors(curr_val) <= self.N:
            i += 1
            curr_val = triangular_number(i)

        return curr_val

    def solve(self):
        self._solve(chad=False)
