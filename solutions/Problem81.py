from helpers import Solution

from os import path

DIRS = path.dirname(path.dirname(path.abspath(__file__)))

DEFAULT_DATA = path.join(DIRS, "data", "Problem81.txt")


class MinimalPathSumOfMatrix(Solution):
    def __init__(self, data_path=DEFAULT_DATA):
        assert path.exists(data_path)

        with open(data_path, 'r') as io_data:
            self.data = io_data.read().strip().split('\n')
            self.data = list(map(lambda x: list(map(int, x.split(","))), self.data))
            self.n, self.m = len(self.data), len(self.data[0])
            self.N = (self.n, self.m)

    def _chad_solution(self):
        for i in range(self.n - 1, -1, -1):
            for j in range(self.m - 1, -1, -1):
                x = 0
                if i < self.n - 1 and j < self.m - 1:
                    x += min(self.data[i + 1][j], self.data[i][j + 1])
                elif i < self.n - 1:
                    x += self.data[i + 1][j]
                elif j < self.m - 1:
                    x += self.data[i][j + 1]

                self.data[i][j] += x
        return self.data[0][0]

    def solve(self):
        self._solve(chad=True)
