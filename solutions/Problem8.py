from helpers import Solution, timeit

from functools import reduce
from os import path

DIRS = path.dirname(path.dirname(path.abspath(__file__)))

DEFAULT_DATA = path.join(DIRS, "data", "Problem8.txt")


class LargestProductInASeries(Solution):
    def __init__(self, n=13, data_path=DEFAULT_DATA):
        assert path.exists(data_path)

        self.N = n
        with open(data_path, 'r') as io_data:
            self.data = io_data.read().replace('\n', '').split('0')

    def _find_sub_solution(self, string_of_digits):
        upper_lim = len(string_of_digits) - self.N + 1
        digits = list(map(lambda x: int(x), string_of_digits))

        max_prod = reduce(lambda x, y: x * y, digits[:self.N])
        running_prod = max_prod

        for i in range(1, upper_lim):
            running_prod //= digits[i-1]
            running_prod *= digits[i+self.N-1]
            if running_prod > max_prod:
                max_prod = running_prod

        return max_prod

    def _baby_solution(self):
        sub_data = filter(lambda x: len(x) >= self.N, self.data)
        return max(map(self._find_sub_solution, sub_data))

    @timeit
    def solve(self):
        self._solve(chad=False)


if __name__ == '__main__':
    prob = LargestProductInASeries()
    prob.solve()
