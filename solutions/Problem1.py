from helpers import Solution


class SumOfMultiplesOf3And5Below(Solution):
    def __init__(self, n=1000):
        super().__init__(n)

    def _baby_solution(self):
        return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(self.N)))

    def _chad_solution(self):
        N = self.N - 1
        nums, coeffs = (3, 5, 15), (1, 1, -1)
        terms = map(lambda x: x * (N // x) * (N // x - 1), nums)
        return sum(map(lambda x: x[1] * x[0], zip(terms, coeffs))) // 2

    def solve(self):
        self._solve(self, chad=True)
