from helpers import Solution


class SumOfLetters(Solution):
    ones = {
        0: 4, 1: 3, 2: 3, 3: 4, 4: 4,
        5: 5, 6: 3, 7: 5, 8: 5, 9: 4,
        10: 3, 11: 6, 12: 6, 13: 8, 14: 8,
        15: 7, 16: 7, 17: 9, 18: 8, 19: 8
    }

    tens = {
        20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6
    }

    def __init__(self, n=5):
        self.N = n

    def length_of_num(self, n):
        if n in self.ones:
            return self.ones[n]
        if n in self.tens:
            return self.tens[n]
        if 20 < n < 100:
            d1, d2 = divmod(n, 10)
            return self.tens[d1 * 10] + self.ones[d2]
        if 100 <= n <= 999:
            d1, d2 = divmod(n, 100)
            return self.ones[d1] + 7 + (d2 != 0) * (self.length_of_num(d2) + 3)
        if 1000 <= n <= 9999:
            d1, d2 = divmod(n, 1000)
            return self.ones[d1] + 8 + (d2 != 0) * (self.length_of_num(d2) + 3)

    def _baby_solution(self):
        return sum(map(self.length_of_num, range(1, self.N + 1)))

    def solve(self):
        self._solve(chad=False)
