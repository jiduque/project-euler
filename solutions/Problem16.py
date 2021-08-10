from helpers import Solution


class PowerDigitSum(Solution):
    def __init__(self, n=1000):
        self.N = n

    def _baby_solution(self):
        return sum(map(int, str(2 ** self.N)))

    def solve(self):
        self._solve(chad=False)
