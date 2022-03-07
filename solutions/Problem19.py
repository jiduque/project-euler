from helpers import Solution

import datetime as dt


class FirstSundays(Solution):
    def __init__(self, n=2000):
        self.a = 1901
        self.N = n

    @staticmethod
    def _helper(year):
        return sum(map(lambda x: dt.date(year, x, 1).weekday() == 6, range(1, 13)))

    def _baby_solution(self):
        return sum(map(FirstSundays._helper, range(self.a, self.N + 1)))

    def solve(self):
        self._solve(chad=False)
