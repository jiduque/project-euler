from helpers import Solution


class DistinctPowers(Solution):
    def __init__(self, n=100):
        self.N = n
        self.lower = 2

    def _baby_solution(self):
        terms = set()
        for i in range(self.lower, self.N + 1):
            for j in range(self.lower, self.N + 1):
                terms.add(i ** j)
        return len(terms)

    def solve(self):
        self._solve(chad=False)
