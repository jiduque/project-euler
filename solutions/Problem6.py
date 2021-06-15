from helpers import Solution


class SumOfSquareDifference(Solution):
    def __init__(self, n=10):
        super().__init__(n)

    def _baby_solution(self):
        vals = range(1, self.N+1)
        t2 = sum(vals) ** 2
        t1 = sum(map(lambda x: x ** 2, vals))
        return t2 - t1

    def _chad_solution(self):
        return self.N * (3*self.N + 2) * (self.N**2 - 1) // 12

    def solve(self):
        self._solve(chad=True)
