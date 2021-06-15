from helpers import Solution
from math import sqrt


def is_prime(k):
    assert k >= 2
    for i in range(2, int(sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True


class LargestPrimeFactorOf(Solution):
    def __init__(self, n=600851475143):
        super().__init__(n)

    def _baby_solution(self):
        largest_prime_factor = 1

        for i in range(2, self.N+1):
            if self.N % i == 0 and is_prime(i) and i > largest_prime_factor:
                largest_prime_factor = i

        return largest_prime_factor

    def _chad_solution(self):
        largest_prime_factor = self.N
        i = 2
        while i * i <= largest_prime_factor:
            while largest_prime_factor % i == 0:
                largest_prime_factor //= i
            i += 1
        return largest_prime_factor

    def solve(self):
        self._solve(chad=True)
