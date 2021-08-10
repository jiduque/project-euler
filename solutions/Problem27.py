from helpers import Solution

from Problem7 import sieve_of_erasthenes


class QuadraticPrimes(Solution):
    def __init__(self, n=1000):
        self.N = n
        self._largest_num = self.N + 2 * self.N ** 2

    def _baby_solution(self):
        primes = set(sieve_of_erasthenes(self._largest_num))
        max_pair, max_num = [0, 0], 0

        for a in range(-self.N, self.N):
            for b in range(-self.N, self.N + 1):
                x = 0
                while x**2 + a*x + b in primes:
                    x += 1

                if x > max_num:
                    max_num = x
                    max_pair[0] = a
                    max_pair[1] = b
        return max_pair[0] * max_pair[1]

    def _chad_solution(self):
        primes = set(sieve_of_erasthenes(self.N))
        bnd = self.N if self.N % 2 else self.N - 1
        max_pair, max_num = [0, 0], 0

        for b in primes:
            for a in range(-bnd, bnd, 2):
                for c in [-1, 1]:
                    x = 0
                    while x**2 + a*x + c*b in primes:
                        x += 1

                    if x > max_num:
                        max_num = x
                        max_pair[0] = a
                        max_pair[1] = c*b

        return max_pair[0] * max_pair[1]

    def solve(self):
        self._solve(chad=True)
